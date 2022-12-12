from sqlalchemy import Column, String, Integer
from db.base_class import Base


class Bug(Base):
    id = Column(Integer, primary_key=True, index=True)
    day = Column(String)
    hour = Column(String)
    description = Column(String)
