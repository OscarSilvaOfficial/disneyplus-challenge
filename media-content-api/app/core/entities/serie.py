from typing import List

class Serie:
  def __init__(self, name: str, description: str, duration: int, categories: List[str]) -> None:
    self.__name = name
    self.__description = description
    self.__duration = duration
    self.__categories = categories

  @property
  def name(self):
    return self.__name

  @property
  def description(self):
    return self.__description

  @property
  def duration(self):
    return self.__duration

  @property
  def categories(self):
    return self.__categories
