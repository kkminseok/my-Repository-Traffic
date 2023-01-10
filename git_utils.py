import github.PaginatedList
import github.Repository
from github import Github


def get_all_repositories(token: str) -> github.PaginatedList.PaginatedList:
    client = Github(token)
    return client.get_user().get_repos("public", "owner")


def get_all_repositories_cloner(repositories: github.PaginatedList.PaginatedList) -> dict:
    cloner_counts = {}
    for repository in repositories:
        unique_cloners = get_clone_traffic_for_repository(repository)
        if unique_cloners == 0:
            continue
        cloner_counts[repository.full_name] = unique_cloners
    return cloner_counts


def get_all_repositories_visitor(repositories: github.PaginatedList.PaginatedList) -> dict:
    views_counts = {}
    for repository in repositories:
        unique_visitor = get_view_traffic_for_repository(repository)
        if unique_visitor == 0:
            continue
        views_counts[repository.full_name] = unique_visitor
    return views_counts


def get_repository(repository_name: str, token: str) -> github.PaginatedList.PaginatedList:
    client = Github(token)
    return client.get_user().get_repo(repository_name)


def get_repository_issue_count(repository_name: str, token: str) -> int:
    return get_repository(repository_name, token).get_issues(labels=["issue"])[0].number


def get_info_last_issue_body(repository_name: str, issue_number: int, token: str) -> str:
    return get_repository(repository_name, token).get_issue(issue_number).body


def create_issue(repo: github.Repository.Repository, title: str, content: str) -> None:
    repo.create_issue(title=title, body=content, labels=["issue"])


def get_clone_traffic_for_repository(repository: github.Repository.Repository) -> int:
    clone_traffic = get_repository_clone_traffic(repository)
    return clone_traffic['uniques']


def get_repository_clone_traffic(repository: github.Repository.Repository) -> dict:
    return repository.get_clones_traffic()


def get_view_traffic_for_repository(repository: github.Repository.Repository) -> int:
    view_traffic = get_repository_view_traffic(repository)
    return view_traffic['uniques']


def get_repository_view_traffic(repository: github.Repository.Repository) -> dict:
    return repository.get_views_traffic()
