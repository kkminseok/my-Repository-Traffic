from dataclasses import dataclass

from data_class.repositories.visitor_repository import VisitorRepository


@dataclass
class VisitorRepositories:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.repositories = dict()
            cls._instance.visitor_sum = 0
        return cls._instance

    '''
    만약 자료구조에 있는데 방문자가 0이면 없애야함.
    '''

    def add_unique_visitor_count(self, repo_full_name: str, visitor_count: int):
        if repo_full_name not in self.repositories:
            self.repositories[repo_full_name] = VisitorRepository(name=repo_full_name.split('/')[1],
                                                                  visitor_count=visitor_count)
            self.visitor_sum += visitor_count
