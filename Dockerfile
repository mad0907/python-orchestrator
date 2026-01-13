FROM python:3.12

WORKDIR /app

COPY orchestrator /app/orchestrator
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "orchestrator.main:app", "--host", "0.0.0.0", "--port", "8000"]
