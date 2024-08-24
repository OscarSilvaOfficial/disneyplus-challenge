from .infra.controllers.series import entrypoint as series_controller

from fastapi import FastAPI

app = FastAPI()

app.include_router(series_controller.router)
