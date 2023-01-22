import github

from module.git_service import get_all_repositories
from pytest_mock import MockerFixture, mocker
from data.repositories.my_repositories import MyRepositories
from data.repositories.repository import Repository


def test_get_all_repositories(mocker: MockerFixture):
    token = "ghp_hbQtNasdzx3xWWoFmpQzxcfslTBs51btjE0sdasd;9"
    mock_repositories = get_repositories_test_object()
    mocker.patch("module.git_api.get_all_repositories", return_value=mock_repositories)
    get_all_repositories(token)
    assert True


def test_singleton():
    my_repositories = MyRepositories.instance()
    repository = Repository(name="123", cloner_count=1, viewer_count=3)
    assert my_repositories.repositories == {}

    my_repositories.add_repository(repository)
    my_repositories2 = MyRepositories.instance()
    assert repository.name in my_repositories2.repositories


def get_repositories_test_object():
    class Repository:
        def __init__(self, full_name):
            self.full_name = full_name
    repository1 = Repository("kkminseok/repository1")
    repository2 = Repository("kkminseok/repository2")

    return [repository1, repository2]



