from data_class.repositories.my_repositories import MyRepositories
from module import git_api
from module.git_api import get_clone_traffic_for_repository

# 실제는 페이지 Repository객체를 넘겨야한다.
def init_all_repositories(token: str) -> MyRepositories:
    repositories = git_api.get_all_repositories(token)
    my_repositories = MyRepositories.instance()
    for repository in repositories:
        print(repository)
        my_repositories.add_repository(repository)


# 실제 Repository정보를 넘겨야한다.
def get_all_repositories_cloner() -> list:
    my_repositories = MyRepositories.instance()
    print(my_repositories.repositories)
    for repository in my_repositories.repositories:
        unique_cloners = get_clone_traffic_for_repository(repository)
        if unique_cloners == 0:
            continue
        my_repositories[repository.name].cloner_count = unique_cloners

        #cloner_counts[repository.full_name] = unique_cloners
    print(my_repositories.repositories)
    pass