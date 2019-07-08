FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN apt-get upgrade
RUN apt-get update && apt-get install -y gettext
RUN pip install -r requirements.txt
EXPOSE 8000