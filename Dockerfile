FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps  \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN apk del .tmp-build-deps

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
