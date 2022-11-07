# main.py


from fastapi import FastAPI, Depends
from pydantic import BaseModel
import uvicorn
from core.config import settings
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# CLASES (?
class Platillo(BaseModel):
    Nombre_Platillo: str
    Foto_URL: str
    Almuerzo_Cena: str
    Entrada: str
    Plato_Fondo: str
    Fruta: str
    Bebida: str


PLATILLOS = []


@app.get("/")
def read_platillos(db: Session = Depends((get_db()))):
    return db.query(models.Comedor).all()


@app.post("/")
def create_Platillo(platillo: Platillo, db: Session = Depends((get_db()))):
    platillo_modelo = models.Comedor()
    platillo_modelo.Nombre_Platillo = platillo.Nombre_Platillo
    platillo_modelo.Bebida = platillo.Nombre_Platillo
    platillo_modelo.Entrada = platillo.Entrada
    platillo_modelo.Foto_URL = platillo.Foto_URL
    platillo_modelo.Almuerzo_Cena = platillo.Almuerzo_Cena
    platillo_modelo.Plato_Fondo = platillo.Plato_Fondo
    platillo_modelo.Fruta = platillo.Fruta

    db.add(platillo_modelo)
    db.commit()

    return platillo


@app.put("/{platillo_id")
def update_platillo(platillo_id: str, platillo: Platillo):
    cont = 0
    for x in PLATILLOS:
        cont += 1
        if x.id_Platillo == platillo_id:
            PLATILLOS[cont - 1] = platillo
            return PLATILLOS


@app.delete("/{platillo_id")
def delete_Platillo(platillo_id: str):
    cont = 0
    for x in PLATILLOS:
        cont += 1
        if x.id_Platillo == platillo_id:
            del PLATILLOS[cont - 1]
            return f"ID: {platillo_id} fue removido"
