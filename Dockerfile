FROM python:3.6

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

RUN pip3 install flask textblob 

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]