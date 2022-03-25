# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /site
COPY requirements.txt /site/
RUN pip install -r requirements.txt
<<<<<<< HEAD
COPY . /site/
# Run application
CMD gunicorn django_heroku.wsgi:application
=======
COPY . /site/
>>>>>>> 830654502dd1d561891c2e54ee2bff991c388409
