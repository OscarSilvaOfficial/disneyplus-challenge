class Serie:
    def __init__(self, name: str, description: str, duration: int, type: str) -> None:
      self.__name = name
      self.__description = description
      self.__duration = duration
      self.__type = type

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
    def type(self):
      return self.__type
