from dataclasses import dataclass


@dataclass
class VisitorRepository:
    name: str
    visitor_count: int

    def __init__(self, name: str, visitor_count: int = 0):
        self.name = name
        self.visitor_count = visitor_count
