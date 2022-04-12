#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from src.process_msg_files import process 
from src.model import Predictor
from src.template_writer import templatize 
from src.read_data_s3 import download, upload 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"

model = Predictor()

@app.route("/extract", methods = ['GET', 'POST'])
def extract():
    try:
        args = request.get_json()
        bucket_name = args["BucketName"]
        download_file_key = args["downloadFileUrl"]
        upload_file_key = args["uploadFileUrl"]
        file_path = download(bucket_name, download_file_key)
        extracts = process(file_path)
        entity_extracts_body = model.predict(extracts["body"])
        entity_extracts_subject = model.predict(extracts["subject"])
        extracts.update(entity_extracts_body)
        extracts.update(entity_extracts_subject)
        response_file = templatize(extracts, f.filename)
        upload(response_file, bucket_name, upload_file_key)
        return jsonify({"status" : 200, "message" : "processed sucessfully"})
    except:
        return jsonify({"status" : 400, "message" : "error in processing"})





if __name__ == "__main__":
    app.run(debug = True)
