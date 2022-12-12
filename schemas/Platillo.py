from typing import Optional
from pydantic import BaseModel


class PlatilloBase(BaseModel):
    id_platillo: str
    nombre_platillo: Optional[str] = None
    foto_url: Optional[str] = None
    entrada: Optional[str] = None
    plato_fondo: Optional[str] = None
    fruta: Optional[str] = None
    bebida: Optional[str] = None


class PlatilloCreate(PlatilloBase):
    id_platillo: str
    nombre_platillo: str
    foto_url: str
    entrada: str
    plato_fondo: str
    fruta: str
    bebida: str


class ShowPlatillo(PlatilloCreate):
    nombre_platillo: str
    foto_url: str

    class Config():
        orm_mode = True
