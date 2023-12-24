from fastapi import APIRouter
from fastapi import status
from starlette.responses import JSONResponse

health_check_route = APIRouter(tags=['health_check'])


@health_check_route.get('/healthcheck', description="health check api")
def health_check():
    return JSONResponse(content={"detail": "health_check", "status": "OK"}, status_code=status.HTTP_200_OK)
