from typing import Optional
from pydantic import BaseModel


class TicketCreate(BaseModel):
    codigo_ticket: str
    numero_turno: str
    estado: bool
    codigo_estudiante: str