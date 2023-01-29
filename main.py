from module.git_api import get_repository_issue_count, get_info_last_issue_body, get_repository
from module.git_service import init_all_repositories, set_all_repositories_cloner, set_all_repositories_visitor, set_all_repositories_today_cloner
from module.issue_utils import create_issue_content
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

    last_issue_number = get_repository_issue_count(repository_name, token)
    last_issue_body = get_info_last_issue_body(repository_name, last_issue_number, token)

    issue_content = create_issue_content(last_issue_body, token)

    print(issue_content)
    repository = get_repository(repository_name, token)
    #create_issue(repository, issue_title, issue_content)

