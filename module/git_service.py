from data.repositories.my_repositories import MyRepositories
from module import git_api


def get_all_repositories(token: str) -> MyRepositories:
    repositories = git_api.get_all_repositories(token)
    my_repositories = MyRepositories.instance()
    for repository in repositories:
        my_repositories.add_repository(repository)
