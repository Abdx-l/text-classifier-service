FROM python:3.12-slim AS dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir -w /wheels -r requirements.txt
FROM python:3.12-slim
WORKDIR /app
COPY --from=dependencies /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -r /wheels && useradd -u 10001 app
COPY . .
USER app
EXPOSE 8000
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
