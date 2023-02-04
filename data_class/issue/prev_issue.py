from dataclasses import dataclass

from data_class.repositories.cloner_repository import ClonerRepository


@dataclass
class PrevIssue:
    title: str
    summary: str
    prev_repository: dict

    def __init__(self, title: str, summary: str):
        self.title = title
        self.summary = summary
        self.prev_repository = dict()

    def add_prev_repository(self, repo_full_name: str, prev_count: int):
        if repo_full_name not in self.prev_repository:
            self.prev_repository[repo_full_name] = ClonerRepository(name=repo_full_name.split('/')[1],
                                                                 today_cloner=prev_count)
