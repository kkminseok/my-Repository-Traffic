import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
from git_utils import get_all_repositories, get_all_repositories_cloner, get_all_repositories_visitor, get_repository_issue_count, get_info_last_issue_body, get_repository, create_issue
from issue_utils import create_issue_content


def sort_items(items: dict) -> list:
    return sorted(items.items(), reverse=True, key=lambda item: item[1])


if __name__ == "__main__":
    load_dotenv()
    today = datetime.now(pytz.timezone('Asia/Seoul'))
    today_date = today.strftime("%Y년 %m월 %d일")
    issue_title = f"오늘자 트래픽 변화({today_date})"

    repository_name = "my-Repository-Traffic"
    token = os.environ['MY_TRAFFIC_TOKEN']

    repositories = get_all_repositories(token)
    sorted_cloner_count = sort_items(get_all_repositories_cloner(repositories))
    sorted_view_count = sort_items(get_all_repositories_visitor(repositories))

    last_issue_number = get_repository_issue_count(repository_name, token)
    last_issue_body = get_info_last_issue_body(repository_name, last_issue_number, token)

    issue_content = create_issue_content(sorted_cloner_count, sorted_view_count, last_issue_body)

    repository = get_repository(repository_name, token)
    create_issue(repository, issue_title, issue_content)



