from abc import ABC, abstractmethod

# Needs creation as a singleton factory
class DB(ABC):
  @abstractmethod
  def query(self, query: str):
    pass

  @abstractmethod
  def create(self, data: dict):
    pass

  @abstractmethod
  def update(self, id: str | int, data: dict):
    pass

  @abstractmethod
  def delete(self, id: str | int):
    pass
