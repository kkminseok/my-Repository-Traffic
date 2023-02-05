from module.git_api import get_repository_issue_count, get_info_last_issue_body, get_repository, create_issue
from module.git_service import init_all_repositories, set_all_repositories_cloner, set_all_repositories_visitor, \
    set_all_repositories_today_cloner, set_all_repositories_today_viewer
from module.issues.issue_utils import create_issue_content, separate_issue
from module.date import get_today
from module.token import get_token

if __name__ == "__main__":
    today_date = get_today()
    issue_title = f"🔅Today's Traffic ({today_date})"

    repository_name = "my-Repository-Traffic"
    token = get_token()

    git_repositories = init_all_repositories(token)

    set_all_repositories_cloner(git_repositories)
    set_all_repositories_today_cloner(token)

    set_all_repositories_visitor(git_repositories)
    set_all_repositories_today_viewer(token)

    last_issue_number = get_repository_issue_count(repository_name, token)
    # 최초인 경우는 바로 이슈를 만든다.
    if last_issue_number is None:
        pass
    else:
        last_issue_body = get_info_last_issue_body(repository_name, last_issue_number, token)
        prev_cloner_info, prev_viewer_info = separate_issue(last_issue_body)
        issue_content = create_issue_content(prev_cloner_info, prev_viewer_info, token)
        repository = get_repository(repository_name, token)
        create_issue(repository, issue_title, issue_content)
