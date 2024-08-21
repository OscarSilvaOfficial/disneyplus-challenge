from app.adapters import db
from types import List
from uuid import uuid4

class MissingFieldException(Exception):
  pass


class MemoryDB(db.DB):
  __data: List[dict]

  def __init__(self, data=[]) -> None:
    super().__init__()
    self.__data: List[dict] = data

  def query(self, query: str):
    return self.__data

  def create(self, data: dict):
    data['uuid'] = uuid4()
    self.__data.append(data)

  def update(self, id: str | int, data: dict):
    for current in self.__data:
      if current['uuid'] == id:
        missing_fields = set(data.keys()) - set(current.keys())

        if missing_fields:
          raise MissingFieldException(f"Missing fields: {', '.join(missing_fields)}")

        current.update(data)

        return current

    raise ValueError(f"'{id}' not found")

  def delete(self, id: str | int):
    for index, current in enumerate(self.__data):
      if current['uuid'] == id:
        self.__data.pop(index)
