import os
from datetime import datetime
from pytz import timezone
from gitUtils import get_all_repositories,\
                     get_all_repositories_traffic,\
                     create_issue,\
                     get_repository,\
                     get_all_repositories_visitor
from issueUtil import create_issue_content

if __name__ == "__main__":
    today = datetime.now(timezone('Asia/Seoul'))
    today_date = today.strftime("%Y년 %m월 %d일")
    issue_title = f"오늘자 트래픽 변화({today_date})"
    repository_name = "my-Repository-Traffic"
    token = os.environ['MY_TRAFFIC_TOKEN']
    #token = ''

    repos = get_all_repositories(token)

    traffic_of_all_repositories = get_all_repositories_traffic(repos)
    view_of_all_repositories = get_all_repositories_visitor(repos)
    sorted_traffic = sorted(traffic_of_all_repositories.items(), reverse=True, key=lambda item: item[1])
    sorted_view = sorted(view_of_all_repositories.items(), reverse=True, key=lambda item: item[1])

    issue_content = create_issue_content(sorted_traffic, sorted_view)

    repository = get_repository(repository_name, token)
    create_issue(repository, issue_title, issue_content)

