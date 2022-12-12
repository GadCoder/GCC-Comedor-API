from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Platillo(Base):
    id_platillo = Column(String, primary_key=True, index=True)
    nombre_platillo = Column(String, nullable=False)
    foto_url = Column(String)
    entrada = Column(String)
    plato_fondo = Column(String)
    fruta = Column(String)
    bebida = Column(String)
