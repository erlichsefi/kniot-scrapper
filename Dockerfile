FROM alpine:3.9

RUN apk add python3 py3-lxml

WORKDIR /usr/src/app

COPY . .

CMD "python3 ./main.py >> print_log.txt" 