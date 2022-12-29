import os
from datetime import datetime

import pytz
from pytz import timezone
from gitUtils import *
from issueUtil import create_issue_content

if __name__ == "__main__":
    print(pytz.VERSION)
    today = datetime.now(timezone('Asia/Seoul'))
    today_date = today.strftime("%Y년 %m월 %d일")
    issue_title = f"오늘자 트래픽 변화({today_date})"
    repository_name = "my-Repository-Traffic"
    token = os.environ['MY_TRAFFIC_TOKEN']
    #token = ''

    repos = get_all_repositories(token)

    cloner_of_all_repositories = get_all_repositories_cloner(repos)
    view_of_all_repositories = get_all_repositories_visitor(repos)
    sorted_cloner = sorted(cloner_of_all_repositories.items(), reverse=True, key=lambda item: item[1])
    sorted_view = sorted(view_of_all_repositories.items(), reverse=True, key=lambda item: item[1])

    last_issue_number = get_repository_issue_count(repository_name, token)
    last_issue_body = get_info_last_issue_body(repository_name, last_issue_number, token)

    issue_content = create_issue_content(sorted_cloner, sorted_view, last_issue_body)

    repository = get_repository(repository_name, token)
    #create_issue(repository, issue_title, issue_content)

