from sqlalchemy.orm import Session
from schemas.Estudiante import EstudianteCreate
from db.models.Estudiante import Estudiante
from core.hashing import Hasher


def create_new_estudiante(estudiante: EstudianteCreate, db: Session):
    estudiante = Estudiante(
        codigo_estudiante=estudiante.codigo_estudiante,
        correo=estudiante.correo,
        password=Hasher.get_password_hash(estudiante.password),
        nombres=estudiante.nombres,
        apellido_pat=estudiante.apellido_pat,
        apellido_mat=estudiante.apellido_mat,
        foto_url=estudiante.foto_url,
        esta_penalizado=False,
        es_jedi=False
    )
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return estudiante


def get_estudiante_by_code(code: str, db: Session):
    estudiante = db.query(Estudiante).filter(
        Estudiante.codigo_estudiante == code).first()
    return estudiante


def get_estudiante_by_email(email: str, db: Session):
    estudiante = db.query(Estudiante).filter(
        Estudiante.correo == email).first()
    return estudiante
