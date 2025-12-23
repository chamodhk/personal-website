FROM python:3.12-slim  

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app 

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt  . 
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .   

RUN python3 manage.py collectstatic --noinput 

EXPOSE 8000

CMD ["gunicorn", "personal_website.wsgi:application", "--bind", "0.0.0.0:8000"]

