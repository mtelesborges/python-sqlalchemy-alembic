FROM python:3.12-alpine

WORKDIR /var/www/app

RUN apk update
RUN apk add --no-cache gcc \
    libc-dev \
    gpgme-dev \
    curl

RUN pip install poetry

RUN mkdir project

COPY pyproject.toml ./
COPY README.md ./
COPY project/__init__.py ./project

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-interaction --no-ansi