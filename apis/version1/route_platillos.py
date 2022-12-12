from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from apis.version1.route_login import get_current_estudiante_from_token
from db.models.Estudiante import Estudiante
from db.session import get_db
from schemas.Platillo import PlatilloCreate, ShowPlatillo
from db.repository.platillos import create_new_platillo, retreive_platillo, retreive_all_platillos

router = APIRouter()


@router.post("/create-platillo/", response_model=ShowPlatillo)
def create_platillo(platillo: PlatilloCreate, db: Session = Depends(get_db), current_user: Estudiante = Depends(get_current_estudiante_from_token)):
    if current_user.es_jedi:
        platillo = create_new_platillo(platillo=platillo, db=db)
        return platillo
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Usuario con codigo {current_user.code} no tiene autorizacion para crear nuevos platos"
    )


@router.get("/get/all")
def read_all_dishes(db: Session = Depends(get_db)):
    platillos = retreive_all_platillos(db)
    if not platillos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se encuentran registros de los platos")
    return platillos


@router.get("/get/{id}", response_model=ShowPlatillo)
def read_dish(id: int, db: Session = Depends(get_db)):
    platillo = retreive_platillo(id=id, db=db)
    if not platillo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dish with this id {id} does not exist")
    return platillo
