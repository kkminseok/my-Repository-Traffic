from dataclasses import dataclass


@dataclass
class ClonerRepository:
    name: str
    cloner_count: int

    def __init__(self, name: str, cloner_count: int = 0):
        self.name = name
        self.cloner_count = cloner_count
