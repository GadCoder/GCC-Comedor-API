from sqlalchemy.orm import Session
from db.models.Estudiante import Estudiante


def get_estudiante(username: str, db: Session):
    user = db.query(Estudiante).filter(Estudiante.correo == username).first()
    return user
