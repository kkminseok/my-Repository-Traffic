import string

import github.Repository
from github import Github


def get_all_repositories(token: string) -> github.Repository.Repository:
    g = Github(token)
    repos = g.get_user().get_repos("public", "owner")
    return repos


def get_all_repositories_traffic(repos: github.Repository.Repository) -> dict:
    traffic_dict = {}
    for repo in repos:
        contents = repo.get_clones_traffic()
        unique_cloner = contents['uniques']
        if unique_cloner == 0:
            continue
        traffic_dict[repo.full_name] = contents['uniques']
    return traffic_dict


def get_repository(repository_name: string, token: string) -> github.Repository.Repository:
    g = Github(token)
    return g.get_user().get_repo(repository_name)


def create_issue(repo: github.Repository.Repository, title: string, content: string):
    repo.create_issue(title=title, body=content)
