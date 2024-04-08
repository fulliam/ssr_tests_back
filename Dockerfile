# FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY . .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]