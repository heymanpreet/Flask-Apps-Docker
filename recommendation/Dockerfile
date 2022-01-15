FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5002

CMD gunicorn --bind 0.0.0.0:5002 main:app