import github.PaginatedList
from github import Github


def get_all_repositories(token: str) -> github.PaginatedList.PaginatedList:
    g = Github(token)
    return g.get_user().get_repos("public", "owner")


def get_all_repositories_cloner(repos: github.PaginatedList.PaginatedList) -> dict:
    cloner_dict = {}
    for repo in repos:
        contents = repo.get_clones_traffic()
        unique_cloner = contents['uniques']
        if unique_cloner == 0:
            continue
        cloner_dict[repo.full_name] = unique_cloner
    return cloner_dict


def get_all_repositories_visitor(repos: github.PaginatedList.PaginatedList) -> dict:
    views_dict = {}
    for repo in repos:
        contents = repo.get_views_traffic()
        unique_visitor = contents['uniques']
        if unique_visitor == 0:
            continue
        views_dict[repo.full_name] = unique_visitor
    return views_dict


def get_repository(repository_name: str, token: str) -> github.PaginatedList.PaginatedList:
    g = Github(token)
    return g.get_user().get_repo(repository_name)


def get_repository_issue_count(repository_name: str, token: str) -> int:
    return get_repository(repository_name, token).get_issues()[0].number


def get_info_last_issue_body(repository_name: str, issue_number: int, token: str) -> str:
    return get_repository(repository_name, token).get_issue(issue_number).body


def create_issue(repo: github.Repository.Repository, title: str, content: str) -> None:
    repo.create_issue(title=title, body=content)
