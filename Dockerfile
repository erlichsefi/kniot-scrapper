FROM arm32v7/python:3.7-slim AS compile-image

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM arm32v7/python:3.7.4-alpine3.9

COPY --from=compile-image /root/.local /root/.local

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT [ "python", "./main.py" ]