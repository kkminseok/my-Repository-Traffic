from dataclasses import dataclass


@dataclass
class VisitorRepository:
    name: str
    visitor_count: int
    today_visitor: int

    def __init__(self, name: str, visitor_count: int = 0, today_visitor: int = 0):
        self.name = name
        self.visitor_count = visitor_count
        self.today_visitor = today_visitor
