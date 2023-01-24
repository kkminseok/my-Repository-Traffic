from dataclasses import dataclass


@dataclass
class Repository:
    name: str
    cloner_count: int
    viewer_count: int
