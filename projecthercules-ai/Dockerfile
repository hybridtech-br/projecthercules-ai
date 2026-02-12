ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.19
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY run.sh /
RUN chmod a+x /run.sh

COPY app /app

WORKDIR /app

CMD [ "/run.sh" ]
