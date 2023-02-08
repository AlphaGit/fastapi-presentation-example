FROM python:3.11.1-alpine AS base
WORKDIR /code

COPY requirements.txt ./requirements.txt
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]