from .infra.controllers import series as series_controller

from fastapi import FastAPI

app = FastAPI()

app.include_router(series_controller.router)
