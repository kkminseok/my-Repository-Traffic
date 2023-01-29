from datetime import datetime

import github.PaginatedList
import pytz

from data_class.repositories.cloner_repositories import ClonerRepositories
from data_class.repositories.visitor_repositories import VisitorRepositories
from module import git_api
from module.util import sort_items


def init_all_repositories(token: str) -> ClonerRepositories:
    return git_api.get_all_repositories(token)


def set_all_repositories_cloner(git_repositories: github.PaginatedList.PaginatedList) -> None:
    """
    모든 깃 레포지토리에 대해서 2주간의 클론 수를 가져온다. 가져오면서 총합도 저장한다.
    :param git_repositories
    :return:
    """
    my_repositories = ClonerRepositories.instance()
    cloner_dict = dict()
    for repository in git_repositories:
        unique_count = git_api.get_all_repositories_cloner(repository)
        if unique_count == 0:
            continue
        cloner_dict[repository.full_name] = unique_count
    sorted_cloner = sort_items(cloner_dict)
    for repo_name, cloner_count in sorted_cloner:
        my_repositories.add_unique_cloner_count(repo_name, cloner_count)


def set_all_repositories_visitor(git_repositories: github.PaginatedList.PaginatedList) -> None:
    my_repositories = VisitorRepositories.instance()
    visitor_dict = dict()
    for repository in git_repositories:
        visitor_count = git_api.get_all_repositories_visitor(repository)
        if visitor_count == 0:
            continue
        visitor_dict[repository.full_name] = visitor_count
    sorted_visitor = sort_items(visitor_dict)
    for repo_name, visitor_count in sorted_visitor:
        my_repositories.add_unique_visitor_count(repo_name, visitor_count)


def set_all_repositories_today_cloner(token: str) -> None:
    """
    모든 레포지토리를 돌면서 오늘 클론한 갯수가 있다면 이를 저장한다.
    :return:
    """
    my_repositories = ClonerRepositories.instance().repositories
    for full_name, repository in my_repositories.items():
        git_repository = git_api.get_repository(repository.name, token)
        today = datetime.now(pytz.timezone('Asia/Seoul'))
        last_cloner = git_api.get_repository_clone_traffic(git_repository)['clones'][-1]

        if today.month == last_cloner.timestamp.month and today.day == last_cloner.timestamp.day:
            repository.today_cloner = last_cloner.uniques
