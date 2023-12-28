import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from elections_app.app.routers.healthcheck import health_check_route
from elections_app.app.routers.v1_elections import v1_elections_routes

# Rename elections_app to app
app = FastAPI(title="Elections API service",
              description="elections",
              version="1.0.0",
              openapi_tags=[{"name": "Elections Service",
                             "description": ""}])

app.include_router(v1_elections_routes)
app.include_router(health_check_route)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.on_event("startup")
def startup_event():
    logging.info('Starting Elections service')


@app.on_event("shutdown")
def shutdown_event():
    logging.info('Shutting down Elections service')
