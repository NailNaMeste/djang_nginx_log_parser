FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY djang_nginx_log_parser .
COPY log_storage .
COPY logs .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8000
