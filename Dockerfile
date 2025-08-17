# syntax=docker/dockerfile:1.7
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN adduser --disabled-password --gecos "" app
WORKDIR /app

FROM base AS builder
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
COPY pyproject.toml ./
COPY requirements/ ./requirements/
# This will fail now, but it's part of the plan
# RUN pip install -r requirements/prod.txt --prefix=/install
COPY app ./app
# Optional: compile bytecode to reduce cold start
RUN python -m compileall -q app

FROM gcr.io/distroless/python3-debian12 AS runtime
USER app
WORKDIR /app
ENV PATH=/usr/local/bin:$PATH
COPY --from=builder /install /usr/local
COPY --from=builder /app /app
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-b", "0.0.0.0:8080", "app.main:app", "--graceful-timeout", "30", "--timeout", "120"]
