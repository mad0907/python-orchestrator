# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time
from contextlib import contextmanager

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://pyorch:pyorch@postgres:5432/pyorch"
)

# Wait for DB before creating engine
def wait_for_db(url, retries=10, delay=3):
    for i in range(retries):
        try:
            engine = create_engine(url)
            conn = engine.connect()
            conn.close()
            print("Database is ready")
            return
        except Exception as e:
            print(f"Waiting for database ({i+1}/{retries})...", e)
            time.sleep(delay)
    raise Exception("Database not available")

wait_for_db(DATABASE_URL)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Correct get_db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
