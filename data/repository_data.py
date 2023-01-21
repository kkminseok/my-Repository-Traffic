from dataclasses import dataclass


@dataclass
class MyRepository:
    name: str
    cloner_count: int
    viewer_count: int