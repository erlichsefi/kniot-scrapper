FROM 581987291365.dkr.ecr.eu-central-1.amazonaws.com/ybaruchel/kniot-scrapper/base-image:latest

COPY . .

CMD [ "python", "./main.py" ]