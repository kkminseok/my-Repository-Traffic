from data_class.repositories.my_repositories import MyRepositories
from module import git_api


def init_all_repositories(token: str) -> MyRepositories:
    repositories = git_api.get_all_repositories(token)
    my_repositories = MyRepositories.instance()
    for repository in repositories:
        my_repositories.add_repository(repository)


def get_all_repositories_cloner() -> list:
    my_repositories = MyRepositories.instance()
    print(my_repositories.repositories)
    for repository in my_repositories.repositories:
        print(repository)
    pass