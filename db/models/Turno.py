from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Turno(Base):
    numero_turno = Column(String, primary_key=True, index=True)
    tickets_disponibles = Column(Integer)
    es_almuerzo = Column(Boolean)
