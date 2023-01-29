import github.PaginatedList

from data_class.repositories.cloner_repositories import ClonerRepositories
from data_class.repositories.visitor_repositories import VisitorRepositories
from module import git_api
from module.util import sort_items


def init_all_repositories(token: str) -> ClonerRepositories:
    return git_api.get_all_repositories(token)


def set_all_repositories_cloner(git_repositories: github.PaginatedList.PaginatedList) -> None:
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