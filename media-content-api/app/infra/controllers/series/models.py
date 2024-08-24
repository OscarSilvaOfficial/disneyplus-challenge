from pydantic import BaseModel

class CreateSerieData(BaseModel):
  name: str
  description: str | None = None
  duration: int
  categories: list