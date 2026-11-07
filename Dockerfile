FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir requests==2.32.3 beautifulsoup4==4.12.3 \
 && useradd -u 1000 -m app
WORKDIR /srv
COPY app/ /srv/
USER app
ENV DATA_DIR=/data PORT=8080
EXPOSE 8080
HEALTHCHECK --interval=60s --timeout=5s CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8080/healthz')"
CMD ["python", "server.py"]
