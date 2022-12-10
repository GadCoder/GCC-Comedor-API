from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Ticket(Base):
    codigo_ticket = Column(String, primary_key=True, index=True)
    numero_turno = Column(Integer, nullable=False)
    estado = Column(Boolean, nullable=False)
    codigo_estudiante = Column(String, ForeignKey("estudiante.codigo_estudiante"))
    estudiante = relationship("Estudiante", back_populates="ticket")


