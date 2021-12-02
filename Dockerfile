FROM python:3.10.0-bullseye

ADD io /io
WORKDIR /io

ENTRYPOINT python
