# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye 

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "flask", "run","--host","0.0.0.0","--port","8000"]
