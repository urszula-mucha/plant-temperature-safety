from dataclasses import dataclass

@dataclass(frozen=True)
class Plant:
    name: str
    min_temperature: float

    # def __init__(self, name: str, min_temperature: float)-> None:
    #     self.name = name
    #     self.min_temperature = min_temperature

    # def __repr__(self) -> str:
    #     return f"Plant(name={self.name}, min_temperature={self.min_temperature})"