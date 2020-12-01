FROM python:3.8.5
MAINTAINER stiub@localhost

COPY requirements/base.txt /app/requirements/base.txt
WORKDIR /app
RUN pip install -r requirements/base.txt

COPY . /app

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]