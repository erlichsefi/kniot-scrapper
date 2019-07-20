FROM arm32v7/python:3-stretch

COPY --from=hypriot/rpi-alpine /usr/bin/qemu-arm-static /usr/bin/qemu-arm-static

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./main.py" ]