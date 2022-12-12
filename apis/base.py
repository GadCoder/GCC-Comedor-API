from fastapi import APIRouter

from apis.version1 import route_estudiantes
from apis.version1 import route_platillos
from apis.version1 import route_login
from apis.version1 import route_bugs
from apis.version1 import route_tickets

api_router = APIRouter()
api_router.include_router(route_estudiantes.router,
                          prefix="/estudiantes", tags=["estudiantes"])
api_router.include_router(
    route_platillos.router, prefix="/platillos", tags=["platillos"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_bugs.router, prefix="/bugs", tags=["bugs"])
api_router.include_router(route_tickets.router,
                          prefix="/tickets", tags=["tickets"])
