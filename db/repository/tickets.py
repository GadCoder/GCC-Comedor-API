from sqlalchemy.orm import Session

from schemas.Ticket import TicketCreate
from db.models.Ticket import Ticket


def create_new_ticket(ticket: TicketCreate, db: Session):
    ticket = Ticket(**ticket.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_number_of_tickets_from_shift(shift: str, db: Session):
    number_of_tickets = db.query(Ticket).filter(Ticket.shift == shift).count()
    return number_of_tickets


def retreative_ticket(code: str, db: Session):
    ticket = db.query(Ticket).filter(Ticket.code == code).first()
    return ticket


def retreative_all_tickets(db: Session):
    tickets = db.query(Ticket).all()
    return tickets
