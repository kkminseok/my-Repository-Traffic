from datetime import datetime
import pytz


def test_get_today_info():
    today = datetime.now(pytz.timezone('Asia/Seoul'))
    assert today.year == 2023
    today_date = today.strftime("%Y년 %m월 %d일")
    issue_title = f"오늘자 트래픽 변화({today_date})"
    print(issue_title)
    assert True

