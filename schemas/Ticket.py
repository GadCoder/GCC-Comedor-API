from typing import Optional
from pydantic import BaseModel


class TicketBase(BaseModel):
    codigo_ticket: str
    numero_turno: str
    estado: Optional[bool] = False
    codigo_estudiante: Optional[str] = None


class TicketCreate(TicketBase):
    codigo_ticket: str
    numero_turno: str
    estado: bool
    codigo_estudiante: str


class ShowTicket(TicketBase):
    codigo_ticket: str
    numero_turno: str
    estado: bool
    codigo_estudiante: str

    class Config():
        orm_mode = True
