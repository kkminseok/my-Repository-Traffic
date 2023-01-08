import os
from datetime import datetime
from zoneinfo import ZoneInfo
from git_utils import *
from issue_utils import create_issue_content


def sort_items(items: dict) -> list:
    return sorted(items.items(), reverse=True, key=lambda item: item[1])


if __name__ == "__main__":
    today = datetime.now(ZoneInfo('Asia/Seoul'))
    today_date = today.strftime("%Y년 %m월 %d일")
    issue_title = f"오늘자 트래픽 변화({today_date})"

    repository_name = "my-Repository-Traffic"
    token = os.environ['MY_TRAFFIC_TOKEN']
    #token = ''

    repos = get_all_repositories(token)
    sorted_cloner = sort_items(get_all_repositories_visitor(repos))
    sorted_view = sort_items(get_all_repositories_cloner(repos))

    last_issue_number = get_repository_issue_count(repository_name, token)
    last_issue_body = get_info_last_issue_body(repository_name, last_issue_number, token)

    issue_content = create_issue_content(sorted_cloner, sorted_view, last_issue_body)

    repository = get_repository(repository_name, token)
    print("complete")
#    create_issue(repository, issue_title, issue_content)


