# main.py

from fastapi import FastAPI, Depends
from core.config import settings
from db.session import engine
from db.base_class import Base


def create_tables():
	Base.metadata.create_all(bind=engine)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	create_tables()       #new
	return app


app = start_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}