""" session.py """
from sqlmodel import Session
from app.db.database import engine

#когда извлекаем из или пишем в бд
def get_session():
    """for working with db"""
    with Session(engine) as session:
        yield session