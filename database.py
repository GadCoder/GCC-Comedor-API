from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "C:/SQLITE3:///./comedor.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same:thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
