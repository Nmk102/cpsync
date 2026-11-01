# Песочница для запуска кода пользователей: компиляторы + исполнитель, без сети (сеть отключается при запуске).
FROM ubuntu:24.04
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends g++ gcc libc6-dev python3 \
 && rm -rf /var/lib/apt/lists/*
COPY runner.py /opt/runner.py
USER 65534:65534
WORKDIR /job
