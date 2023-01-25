from module.git_service import init_all_repositories, get_all_repositories_cloner
from pytest_mock import MockerFixture, mocker
from data_class.repositories.my_repositories import MyRepositories
from data_class.repositories.repository import Repository
from tests.data_class_test.my_repositories_test import TestMyRepositories


def test_get_all_repositories(mocker: MockerFixture):
    token = "ghp_hbQtNasdzx3xWWoFmpQzxcfslTBs51btjE0sdasd;9"
    mock_repositories = get_repositories_test_object()
    mocker.patch("module.git_api.get_all_repositories", return_value=mock_repositories)
    init_all_repositories(token)
    assert True


def test_get_all_repositories_cloner(mocker: MockerFixture):
    instance = MyRepositories
    mock_repositories = get_repositories_test_object()
    mocker.patch.object(instance, "instance", return_value=mock_repositories)
    get_all_repositories_cloner()
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
        def __init__(self, name):
            self.name = name
    repository1 = Repository(name="kkminseok/repository1")
    repository2 = Repository(name="kkminseok/repository2")
    repositories = TestMyRepositories.instance()
    repositories.add_repository(repository1)
    repositories.add_repository(repository2)
    return repositories



