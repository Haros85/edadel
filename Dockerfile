FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY ./code /app

EXPOSE 8000

CMD ["gunicorn", "--chdir", "foodgram", "--bind", ":8000", "foodgram.wsgi:application"]