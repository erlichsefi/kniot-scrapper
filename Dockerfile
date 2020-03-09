FROM alpine:3.9

RUN apk add python3 py3-lxml

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT [ "python3", "./main.py" ]