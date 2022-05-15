from fastapi import FastAPI, Response, Request
from settings import get_settings
import routers as psql_routers
from apps.employee_routers.routers import router as employee_routers
print(get_settings())
print(psql_routers.init())

app = FastAPI()

app.include_router(employee_routers, prefix="/employee")
# app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
# app.include_router(assets_router.router)
