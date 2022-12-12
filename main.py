from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from apis.base import api_router
from db.session import engine
from db.base import Base


def include_router(app):
    app.include_router(api_router)


def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    create_tables()
    return app


app = start_application()
