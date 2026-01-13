from fastapi import FastAPI
from .database import engine, Base
from .routers import bots, jobs, logs, health

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(bots.router)
app.include_router(jobs.router)
app.include_router(logs.router)
app.include_router(health.router)
