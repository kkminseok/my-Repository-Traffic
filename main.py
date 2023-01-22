from module.git_api import get_all_repositories_cloner, get_all_repositories_visitor, get_repository_issue_count, get_info_last_issue_body, get_repository
from module.git_service import get_all_repositories
from module.issue_utils import create_issue_content
from module.date import get_today
from module.token import get_token


def sort_items(items: dict) -> list:
    return sorted(items.items(), reverse=True, key=lambda item: item[1])


if __name__ == "__main__":
    today_date = get_today()
    issue_title = f"🔅Today's Traffic ({today_date})"

    repository_name = "my-Repository-Traffic"
    token = get_token()

    repositories = get_all_repositories(token)

    sorted_cloner_count = sort_items(get_all_repositories_cloner(repositories))
    sorted_view_count = sort_items(get_all_repositories_visitor(repositories))

    last_issue_number = get_repository_issue_count(repository_name, token)
    last_issue_body = get_info_last_issue_body(repository_name, last_issue_number, token)

    issue_content = create_issue_content(sorted_cloner_count, sorted_view_count, last_issue_body, token)

    print(issue_content)
    repository = get_repository(repository_name, token)
    #create_issue(repository, issue_title, issue_content)



