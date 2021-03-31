FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN apt update && apt-get -y install \
    build-essential \
    python3-dev
RUN mkdir /code
COPY . /code/
WORKDIR /code/scrummage/requirements
RUN pip install --upgrade pip && pip install wheel && pip install -r common.txt
WORKDIR /code
RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]
