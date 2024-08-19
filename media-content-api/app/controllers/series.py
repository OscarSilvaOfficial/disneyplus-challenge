from typing import Union

from fastapi import APIRouter

router = APIRouter(
    prefix="/series",
    tags=["series"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_series():
    return
