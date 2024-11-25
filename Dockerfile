FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.12-slim
WORKDIR /app

# Copiar os pacotes instalados do builder
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /app /app

RUN adduser --disabled-password --no-create-home django-user
USER django-user

EXPOSE 8000