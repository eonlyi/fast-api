""" main.py """
from fastapi import FastAPI
from app.db.database import init_db
from app.routes import tasks, auth

app = FastAPI()

@app.on_event("startup")
def on_startup():
    """ Function to start """
    init_db()

app.include_router(tasks.router)
app.include_router(auth.router)