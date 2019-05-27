FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN apt-get upgrade
#RUN pip install -r requirements.txt
RUN pip install django
RUN pip install psycopg2
RUN pip install djongo
RUN apt-get update && apt-get install -y gettext
RUN pip install django-crispy-forms
RUN pip install django-redis
EXPOSE 8000