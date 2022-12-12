from typing import Optional
from pydantic import BaseModel, EmailStr


class EstudianteCreate(BaseModel):
    codigo_estudiante: str
    correo: EmailStr
    password: str
    nombres: str
    apellido_pat: str
    apellido_mat: str
    foto_url: str
    esta_penalizado: bool
    es_jedi: bool


class ShowEstudiante(BaseModel):
    correo: EmailStr
    codigo_estudiante: str
    esta_penalizado: bool

    class Config():  # convert dict or non dict obj to json
        orm_mode = True


class ShowFullEstudiante(BaseModel):
    correo: EmailStr
    codigo_estudiante: str
    nombres: str
    apellido_pat: str
    apellido_mat: str
    foto_url: str
    es_jedi: bool

    class Config():  # convert dict or non dict obj to json
        orm_mode = True
