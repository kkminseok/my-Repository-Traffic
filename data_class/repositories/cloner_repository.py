from dataclasses import dataclass


@dataclass
class ClonerRepository:
    name: str
    cloner_count: int
    today_cloner: int

    def __init__(self, name: str, cloner_count: int = 0, today_cloner: int =0):
        self.name = name
        self.cloner_count = cloner_count
        self.today_cloner = today_cloner
    
