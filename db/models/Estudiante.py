from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Estudiante(Base):
    codigo_estudiante = Column(String, primary_key=True, index=True)
    correo = Column(String, nullable=False)
    password = Column(String, nullable=False)
    nombres = Column(String, nullable=False)
    apellido_pat = Column(String, nullable=False)
    apellido_mat = Column(String, nullable=False)
    foto_url = Column(String, nullable=True)
    esta_penalizado = Column(Boolean, nullable=False)
    ticket = relationship("Ticket", back_populates="estudiante")
    es_jedi = Column(Boolean)
