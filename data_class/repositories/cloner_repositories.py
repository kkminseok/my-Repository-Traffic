from dataclasses import dataclass

from data_class.repositories.clonerrepository import ClonerRepository


@dataclass
class ClonerRepositories:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.repositories = dict()
        return cls._instance

    '''
    만약 자료구조에 있는데 클로너가 0이면 없애야함. 이또한 비용으로 작용할 듯해서
    기존 레포지토리에 저장하던 로직은 삭제
    '''
    def add_unique_cloner_count(self, repo_full_name: str, cloner_count: int):
        if repo_full_name not in self.repositories:
            self.repositories[repo_full_name] = ClonerRepository(name=repo_full_name.split('/')[1], cloner_count=cloner_count)

