FROM arm32v7/alpine:3.9

COPY --from=hypriot/rpi-alpine /usr/bin/qemu-arm-static /usr/bin/qemu-arm-static

RUN apk add python3 py3-lxml

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT [ "pip3", "list" ]