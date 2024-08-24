from fastapi import APIRouter
from app.adapters.__mock import series_data
from app.infra.db import memory

router = APIRouter(
    prefix="/series",
    tags=["series"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get():
    db = memory.MemoryDB(data=series_data)
    return

@router.post("/")
def create_series():
    return
