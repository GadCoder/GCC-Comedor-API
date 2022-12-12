from typing import Optional
from pydantic import BaseModel, EmailStr


class EstudianteCreate(BaseModel):
    codigo_estudiante: str
    correo: EmailStr
    nombres: str
    apellido_pat: str
    apellido_mat: str
    foto_url: str
    esta_penalizado: bool
