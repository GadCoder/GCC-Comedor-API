from sqlalchemy.orm import Session
from schemas.Estudiante import EstudianteCreate
from db.models.Estudiante import Estudiante
from core.hashing import Hasher
import requests


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



def get_estudiante(email: str, password: str, db: Session):
    url = 'https://sumvirtual.unmsm.edu.pe/sumapi/loguearse'
    headers = {
        'accept': 'application/json',
        'Accept-Encoding': 'gzip',
        'authorization': 'AUTH TOKEN',
        'Connection': 'Keep-Alive',
        'Content-Length': '52',
        'Content-Type': 'application/json',
        'Host': 'sumvirtual.unmsm.edu.pe',
        'User-Agent': 'okhttp/4.9.2'
    }
    data = {
        'usuario': email,
        'clave': password
    }
    request = requests.post(url, headers=headers, json=data)
    status = request.status_code
    if status != 200:
        return None
    data = request.json()['data'][-1]['dto']
    estudiante = Estudiante(
        codigo_estudiante=data['codAlumno'],
        correo=f"{email}@unmsm.edu.pe",
        password=password,
        nombres=data['nomAlumno'],
        apellido_pat=data['apePaterno'],
        apellido_mat=data['apeMaterno'],
        foto_url=data['foto'],
        esta_penalizado=False,
        es_jedi=False
    )
    if get_estudiante_by_code(estudiante.codigo_estudiante, db=db) is None:
        create_new_estudiante(estudiante, db=db)
    return estudiante


def get_estudiante_by_code(code: str, db: Session):
    estudiante = db.query(Estudiante).filter(
        Estudiante.codigo_estudiante == code).first()
    return estudiante


def get_estudiante_by_email(email: str, db: Session):
    estudiante = db.query(Estudiante).filter(
        Estudiante.correo == email).first()
    return estudiante
