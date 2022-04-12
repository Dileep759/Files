#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import io
import pandas as pd
import json

def download(bucket_name, file_key):
    session = boto3.session.Session()
    try:
        s3.Bucket(bucket_name).download_file(file_key, f'./uplods/{file_key}')
        return f'./uploads/{file_key}'
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("object does not exist")
        else:
            raise
        
def upload(file_name, bucket_name, file_key):
    session = boto3.resource('s3')
    s3.meta.client.upload_file(file_name, bucket_name, file_key)


