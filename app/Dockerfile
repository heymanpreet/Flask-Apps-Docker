FROM python:3.8

COPY requirements.txt ./requirements.txt
COPY app1.py ./app1.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app1:app