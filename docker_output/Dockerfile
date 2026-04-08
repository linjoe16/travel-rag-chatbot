# syntax=docker/dockerfile:1
FROM python:3.11-slim
WORKDIR /
RUN apt-get update && apt-get install -y runit gcc && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && \
    pip install promptflow==1.18.4 promptflow-tools keyrings.alt gunicorn==22.0.0 "uvicorn>=0.27.0,<1.0.0" azure-search-documents
COPY ./flow /flow
EXPOSE 8080
COPY ./connections /connections
RUN rm -rf /var/runit
COPY ./runit /var/runit
RUN chmod -R +x /var/runit
COPY ./start.sh /
CMD ["bash", "./start.sh"]
