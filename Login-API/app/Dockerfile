FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5001 login:app