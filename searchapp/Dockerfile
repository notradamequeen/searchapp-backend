FROM python:3.7.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /searchapp/
WORKDIR /searchapp/
ADD requirements /searchapp/requirements/

RUN pip install -U pip
RUN pip install -r requirements/requirements.txt

ADD . /searchapp/
RUN chmod +x docker-entrypoint.sh
copy ./docker-entrypoint.sh /tmp
ENTRYPOINT ["sh", "/tmp/docker-entrypoint.sh"]
