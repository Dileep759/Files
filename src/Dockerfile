FROM python:3.7
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN pip3 install gunicorn
COPY . /app
WORKDIR /app
ENTRYPOINT ["./start.sh"]

