from datetime import datetime
import pytz


def get_today() -> datetime:
    today = datetime.now(pytz.timezone('Asia/Seoul'))
    return today.strftime("%Y년 %m월 %d일")