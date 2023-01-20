from datetime import datetime
import re
import pandas as pd
import pytz


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