""" database.py """
from sqlmodel import create_engine, SQLModel

engine = create_engine('sqlite:///./urls.db')

def init_db():
    """Tdb initialixation"""
    SQLModel.metadata.create_all(engine)