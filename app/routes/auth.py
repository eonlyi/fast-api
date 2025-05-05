""" auth.py """
from fastapi import HTTPException,APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from app.db.session import get_session
from app.models.models import User
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.schemas import Token

router = APIRouter(prefix="/auth", tags=["Безопасность"])

@router.post("/register")
def register(username: str, password: str, email: str, session = Depends(get_session)):
    """Function check register"""
    user_exists = session.exec(select(User).where(User.username == username)).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    user = User(username=username, hashed_password=hash_password(password), email=email)
    session.add(user)
    session.commit()
    return{"message":"Пользователь зарегистрирован"}

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session = Depends(get_session)):
    """Function check login"""
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    access_token = create_access_token(data={"sub":user.username})
    return{"access_token": access_token, "token_type": "bearer"}
