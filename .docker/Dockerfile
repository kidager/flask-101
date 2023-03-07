FROM python:3.11-alpine

RUN apk --no-cache --update add \
    bash \
    && rm -rf /var/cache/apk/*

WORKDIR /code

RUN pip install gunicorn

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./.docker/gunicorn_conf.py /etc/gunicorn_conf.py

CMD ["gunicorn", "--conf", "/etc/gunicorn_conf.py", "--bind", "0.0.0.0:80", "app.main:app"]
