from dataclasses import dataclass

from data_class.repositories.repository import Repository


@dataclass
class TestMyRepositories:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.repositories = dict()
        return cls._instance

    def add_repository(self, repository: Repository):
        self.repositories[repository.name] = repository