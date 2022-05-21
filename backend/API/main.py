from fastapi import FastAPI, Response, Request
from settings import get_settings
import routers as psql_routers
from apps.employee_routers.routers import router as employee_routers
from apps.client_routers.routers import router as client_routers
print(get_settings())
print(psql_routers.init())

app = FastAPI()

app.include_router(employee_routers, prefix="/employee")
app.include_router(client_routers, prefix="/client", tags=["auth"])
# app.include_router(assets_router.router)
