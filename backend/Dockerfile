FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1
ENV GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgdal.so.30  
ENV GEOS_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgeos_c.so.1
ENV VIRTUAL_ENV /.env
ENV PATH /env/bin:$PATH

WORKDIR usr/src/app


RUN apt-get update && apt-get install -y \
    build-essential \ 
    libpq-dev \ 
    && rm -rf /var/lib/apt/lists/*
 


COPY . .
COPY requirements.txt .



EXPOSE 8000


EXPOSE 8000



RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","manage.py","runserver"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi:application"]