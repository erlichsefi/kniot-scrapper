FROM arm32v7/python:3.7.4-alpine3.9

RUN apk add gcc musl-dev libffi-dev

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./main.py" ]