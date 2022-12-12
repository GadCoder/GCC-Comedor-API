from sqlalchemy.orm import Session
from schemas.bugs import BugCreate
from db.models.bugs import Bug


def create_new_bug(bug: BugCreate, db: Session):
    bug_object = Bug(**bug.dict())
    db.add(bug_object)
    db.commit()
    db.refresh(bug_object)
    return bug_object


def retreive_bug(id: int, db: Session):
    bug = db.query(Bug).filter(Bug.id == id).first()
    return bug


def retreive_all_bugs(db: Session):
    bugs = db.query(Bug).all()
    return bugs