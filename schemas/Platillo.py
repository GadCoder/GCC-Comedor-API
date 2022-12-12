from typing import Optional
from pydantic import BaseModel


class PlatilloCreate(BaseModel):
    id_platillo: str
    nombre_platillo: str
    foto_url: str
    entrada: str
    plato_fondo: str
    fruta: str
    bebida: str
