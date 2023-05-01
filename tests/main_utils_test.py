from datetime import datetime
import re
import pandas as pd
import pytz

from data_class.repositories.cloner_repositories import ClonerRepositories, ClonerRepository
from module.issues.prev_issue_viewer_utils import get_today_count


def test_get_today_info():
    today = datetime.now(pytz.timezone('Asia/Seoul'))
    assert today.year == 2023
    today_date = today.strftime("%Y년 %m월 %d일")
    issue_title = f"오늘자 트래픽 변화({today_date})"
    print(issue_title)
    assert True


def test_compare_datetime():
    today = datetime.now(pytz.timezone('Asia/Seoul'))
    pandas_today = pd.Timestamp('2023-01-19 00:00:00')
    assert today.month == pandas_today.month
    assert today.day == pandas_today.day


def test_regrex_search():
    my_traffic_data = 'clone of kkminseok/my-Repository-Traffic: 17 (🔽-6) / today: 2'
    match = re.findall(r'(\d+)', my_traffic_data)
    if match:
        print(match)


def test_get_today_count():
    test_str = 'view of [kkminseok/real-world-springboot-vue.js](https://github.com/kkminseok/real-world-springboot-vue.js): 89 (🔼1)/ today: 3 '
    get_today_count(test_str)


def test_data_class():
    my_repositories = ClonerRepositories(repositories={})
    repository = ClonerRepository(name="123", cloner_count=1, viewer_count=3)
    repository2 = ClonerRepository(name="1234", cloner_count=1, viewer_count=3)
    my_repositories.repositories[repository.name] = repository
    my_repositories.repositories[repository2.name] = repository2

    assert len(my_repositories.repositories) == 2
