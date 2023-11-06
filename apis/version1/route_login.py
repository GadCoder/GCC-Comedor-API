from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status, HTTPException
from db.session import get_db
from core.hashing import Hasher
from schemas.tokens import Token
from db.repository.login import get_estudiante
from core.security import create_access_token
from core.config import settings
import requests

router = APIRouter()


def authenticate_estudiante(username: str, password: str, db: Session):
    user = get_estudiante(username=username, db=db)
    print(user.correo)
    print(user.password)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user


@router.post("/get-token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    url = 'https://sumvirtual.unmsm.edu.pe/sumapi/loguearse'
    headers = {
        'accept': 'application/json',
        'Accept-Encoding': 'gzip',
        'authorization': 'AUTH TOKEN',
        'Connection': 'Keep-Alive',
        'Content-Length': '52',
        'Content-Type': 'application/json',
        'Host': 'sumvirtual.unmsm.edu.pe',
        'User-Agent': 'okhttp/4.9.2'
    }
    data = {
        'usuario': form_data.username,
        'clave': form_data.password
    }
    request = requests.post(url, headers=headers, json=data)
    request_status = request.status_code
    if request_status != 200:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrecta"
        )
    data = request.json()
    token = data['data'][-1]['token']
    access_token = f'Bearer {token}'
    cookies = request.cookies

    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie.name] = cookie.value
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/get-token")


def get_current_estudiante_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        print(f"email extracted is {username}")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_estudiante(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user
