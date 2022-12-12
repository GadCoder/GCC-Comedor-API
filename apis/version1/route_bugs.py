from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from schemas.bugs import BugCreate, ShowBug
from db.repository.bugs import create_new_bug, retreive_bug, retreive_all_bugs

router = APIRouter()


@router.post("/create-bug/", response_model=ShowBug)
def create_bug(bug: BugCreate, db: Session = Depends(get_db)):
    bug = create_new_bug(bug=bug, db=db)
    return bug


@router.get("/get/all")
def read_all_bugs(db: Session = Depends(get_db)):
    bugs = retreive_all_bugs(db)
    if not bugs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se encuentran los bugs")
    return bugs


@router.get("/get/{id}", response_model=ShowBug)
def read_bug(id: int, db: Session = Depends(get_db)):
    bug = retreive_bug(id=id, db=db)
    if not bug:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bug con id {id} no existe")
    return bug
