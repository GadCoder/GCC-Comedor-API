
from sqlalchemy.orm import Session
from schemas.Platillo import PlatilloCreate
from db.models.Platillo import Platillo


def create_new_platillo(platillo: PlatilloCreate, db: Session):
    platillo_object = Platillo(**platillo.dict())
    db.add(platillo_object)
    db.commit()
    db.refresh(platillo_object)
    return platillo_object


def retreive_platillo(id: int, db: Session):
    item = db.query(Platillo).filter(Platillo.id == id).first()
    return item


def retreive_all_platillos(db: Session):
    platillos = db.query(Platillo).all()
    return platillos
