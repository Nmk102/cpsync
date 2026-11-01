# Приложение CP Sync (сайт + API). Код пользователей запускается в отдельных контейнерах cpsync-sandbox.
FROM python:3.12-slim
RUN pip install --no-cache-dir segno==1.6.6
WORKDIR /app
COPY server/cpsync /app/cpsync
COPY server/sandbox /app/sandbox
COPY server/web /app/web
COPY dist /app/dist
ENV PYTHONUNBUFFERED=1 \
    CPSYNC_DATA=/var/lib/cpsync \
    CPSYNC_PORT=8080 \
    CPSYNC_PLUGIN_ZIP=/app/dist/cpsync-plugin.zip
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/healthz', timeout=4)"
CMD ["python", "-m", "cpsync"]
