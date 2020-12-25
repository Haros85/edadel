FROM python:3.8

RUN mkdir /code

WORKDIR /code

COPY ./code /code
COPY ./fixtures /code

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip install -r /code/requirements.in

RUN python manage.py collectstatic --noinput