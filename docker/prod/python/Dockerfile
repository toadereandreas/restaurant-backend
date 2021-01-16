FROM python:3.8.5
MAINTAINER stiub@localhost

COPY requirements/base.txt /app/requirements/base.txt
COPY requirements/prod.txt /app/requirements/prod.txt
WORKDIR /app
RUN pip install -r requirements/prod.txt

COPY . /app

COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]