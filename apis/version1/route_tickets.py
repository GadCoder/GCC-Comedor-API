from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from schemas.Ticket import TicketCreate, ShowTicket
from db.session import get_db
from db.repository.tickets import create_new_ticket, get_number_of_tickets_from_shift, retreative_ticket, \
    retreative_all_tickets

router = APIRouter()


@router.post("/create-ticket/", response_model=ShowTicket)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket = create_new_ticket(ticket=ticket, db=db)
    return ticket


@router.get("/get-all-tickets")
def get_all_tickets(db: Session = Depends(get_db)):
    tickets = retreative_all_tickets(db)
    if not tickets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se encuentran los tickeds")
    return tickets


@router.get("/get-shift-tickets/{shift}")
def get_tickets_from_shift(shift: str, db: Session = Depends(get_db)):
    tickets = get_number_of_tickets_from_shift(shift, db)
    if not tickets:
        return 0
    return tickets


@router.get("/get-ticket-info/{code}", response_model=ShowTicket)
def get_ticket_info(code: str, db: Session = Depends(get_db)):
    ticket = retreative_ticket(code, db)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se encuentra el ticket")
    return ticket
