FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk --no-cache --update add \
    bash \
    && rm -rf /var/cache/apk/*

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

COPY ./requirements.txt /var/www/requirements.txt

RUN pip install -r /var/www/requirements.txt

# COPY . /var/www/
