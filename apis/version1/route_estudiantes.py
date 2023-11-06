from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.models.Estudiante import Estudiante
from schemas.Estudiante import EstudianteCreate, ShowEstudiante, ShowFullEstudiante
from db.session import get_db
from db.repository.estudiantes import create_new_estudiante, get_estudiante_by_code, get_estudiante
from apis.version1.route_login import get_current_estudiante_from_token
from fastapi import status, HTTPException

router = APIRouter()


@router.post("/create-estudiante/", response_model=ShowEstudiante)
def create_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    estudiante = create_new_estudiante(estudiante=estudiante, db=db)
    return estudiante



@router.get("/read-estudiante/", response_model=ShowFullEstudiante)
def read_estudiante(email: str, password: str, db: Session = Depends(get_db)):
    estudiante = get_estudiante(email=email, password=password, db=db)
    
    return estudiante
