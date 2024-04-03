FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /job-portal/backend

COPY requirements.txt .


EXPOSE 8000

CMD ["python","manage.py","runserver"]

RUN pip install --no-cache-dir -r requirements.txt

RUN gunicorn backend.wsgi:application --bind 0.0.0.0:8000