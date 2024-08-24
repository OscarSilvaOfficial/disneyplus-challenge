from fastapi import APIRouter, Response, status

from app.infra.db import memory
from .models import CreateSerieData
from .__mock import series_data

router = APIRouter(
  prefix="/series",
  tags=["series"],
  responses={
    404: {
      "description": "Not found"
    }
  },
)

@router.get("")
def get(response: Response):
  db = memory.MemoryDB(data=series_data)
  data = db.query('SELECT * FROM series')

  is_empty_data = len(data) == 0
  if is_empty_data:
    response.status_code = status.HTTP_404_NOT_FOUND
    return

  return data

@router.post("", status_code=201)
def create_series(serie: CreateSerieData):
  return serie
