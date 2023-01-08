import github.PaginatedList
from pytest_mock import MockerFixture

from git_utils import *


def test_get_all_repositories(token: str):
    get_all_repositories(token)
    assert True


def test_get_all_repositories_cloner(repositories: github.PaginatedList.PaginatedList, mocker: MockerFixture):
    mocker.patch("git_utils.get_repository_clone_traffic", return_value={"uniques": 100})
    result = get_all_repositories_cloner(repositories)
    assert len(result) == 3
    assert result['kkminseok.repo1'] == 100
    assert result['kkminseok.repo2'] == 100
    assert result['kkminseok.repo3'] == 100


def test_get_all_repositories_cloner(repositories: github.PaginatedList.PaginatedList, mocker: MockerFixture):
    mocker.patch("git_utils.get_repository_view_traffic", return_value={"uniques": 100})
    result = get_all_repositories_visitor(repositories)
    assert len(result) == 3
    assert result['kkminseok.repo1'] == 100
    assert result['kkminseok.repo2'] == 100
    assert result['kkminseok.repo3'] == 100
