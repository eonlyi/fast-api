""" schemas.py """
from pydantic import BaseModel

class Token(BaseModel):
    """ Class for token """
    access_token: str
    token_type: str