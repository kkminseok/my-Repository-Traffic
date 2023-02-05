from dataclasses import dataclass
import re

from data_class.repositories.cloner_repository import ClonerRepository
from data_class.repositories.visitor_repository import VisitorRepository


@dataclass
class PrevIssue:
    title: str
    title_count: int
    summary: str
    prev_repositories: dict

    def __init__(self, title: str, summary: str):
        self.title = title
        self.title_count = get_title_count(title)
        self.summary = summary
        self.prev_repositories = dict()

    def add_prev_cloner_repository(self, repo_full_name: str, two_week_count: int, today_count: int):
        if repo_full_name not in self.prev_repositories:
            self.prev_repositories[repo_full_name] = ClonerRepository(name=repo_full_name.split('/')[1],
                                                                      cloner_count=two_week_count,
                                                                      today_cloner=today_count)

    def add_prev_viewer_repository(self, repo_full_name: str, two_week_count: int, today_count: int):
        if repo_full_name not in self.prev_repositories:
            self.prev_repositories[repo_full_name] = VisitorRepository(name=repo_full_name.split('/')[1],
                                                                       visitor_count=two_week_count,
                                                                       today_visitor=today_count)


def get_title_count(title: str) -> int:
    idx = title.find(':')
    return int(re.sub(r'[^0-9]', '', title[idx:title.find('(', idx)]))
