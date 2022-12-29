import string

import github.PaginatedList
from github import Github


def get_all_repositories(token: string) -> github.PaginatedList.PaginatedList:
    g = Github(token)
    return g.get_user().get_repos("public", "owner")


def get_all_repositories_traffic(repos: github.PaginatedList.PaginatedList) -> dict:
    traffic_dict = {}
    for repo in repos:
        contents = repo.get_clones_traffic()
        unique_cloner = contents['uniques']
        if unique_cloner == 0:
            continue
        traffic_dict[repo.full_name] = unique_cloner
    return traffic_dict


def get_all_repositories_visitor(repos: github.PaginatedList.PaginatedList) -> dict:
    views_dict = {}
    for repo in repos:
        contents = repo.get_views_traffic()
        unique_visitor = contents['uniques']
        if unique_visitor == 0:
            continue
        views_dict[repo.full_name] = unique_visitor
    return views_dict


def get_repository(repository_name: string, token: string) -> github.PaginatedList.PaginatedList:
    g = Github(token)
    return g.get_user().get_repo(repository_name)


def create_issue(repo: github.Repository.Repository, title: string, content: string):
    repo.create_issue(title=title, body=content)
