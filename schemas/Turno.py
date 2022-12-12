from typing import Optional
from pydantic import BaseModel


class TurnoCreate(BaseModel):
    numero_turno: str
    tickets_disponibles: int
    es_almuerzo: bool

