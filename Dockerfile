FROM 581987291365.dkr.ecr.us-east-1.amazonaws.com/ybaruchel/kniot-scrapper/base-image

COPY . .

CMD [ "python", "./main.py" ]