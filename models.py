from sqlalchemy import Column, String
from database import Base


class Comedor(Base):
    __tablename__ = "Platillos"

    ID_Platillo = Column(String, primary_key=True, index=True)
    Nombre_Platillo = Column(String)
    Foto_URL = Column(String)
    Almuerzo_Cena = Column(String)
    Entrada = Column(String)
    Plato_Fondo = Column(String)
    Fruta = Column(String)
    Bebida = Column(String)
