from fastapi.testclient import TestClient
from fastapi import FastAPI

from app.infra.controllers.series.entrypoint import router

app = FastAPI()

app.include_router(router)

client = TestClient(app)

def test_get_series():
  response = client.get("/series")
  assert response.status_code == 200

def test_create_series():
  response = client.post(
    "/series", 
    json={
      'name': 'Serie test',
      'description': 'Description test',
      'duration': 2,
      'categories': ['Serie test'],
    }
  )

  assert response.status_code == 201