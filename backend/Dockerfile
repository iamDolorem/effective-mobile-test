FROM python:3.12-alpine

WORKDIR /app
COPY app.py /app/app.py

RUN addgroup -S app && adduser -S app -G app
USER app

EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/', timeout=2).read()"

CMD ["python", "/app/app.py"]
