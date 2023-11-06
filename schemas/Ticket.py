from typing import Optional
from pydantic import BaseModel


class TicketBase(BaseModel):
    codigo_ticket: str
    numero_turno: int
    estado: Optional[bool] = False
    hora: Optional[str] = None
    codigo_estudiante: Optional[str] = None


class TicketCreate(TicketBase):
    pass


class ShowTicket(TicketBase):


    class Config():
        orm_mode = True
