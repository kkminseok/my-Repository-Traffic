from constant.constant import CLONER_TITLE
from data_class.issue.prev_issue import PrevIssue
from data_class.repositories.cloner_repositories import ClonerRepositories
from data_class.repositories.visitor_repositories import VisitorRepositories


def separate_issue(last_issue_body: str):
    prev_issue_cloner = get_last_issue_cloner(last_issue_body)
    print(prev_issue_cloner)
    pass


# TODO Refacotring...
def create_issue_content(last_issue_body: str, token: str) -> str:
    # 문자열 그냥 합치면 효율성이 떨이짐.
    github_url = 'https://github.com/'
    issue_list = []
    cloner_data = ClonerRepositories.instance().repositories
    view_data = VisitorRepositories.instance().repositories
    total_cloner_sum = ClonerRepositories.instance().cloner_sum
    total_viewer_sum = VisitorRepositories.instance().visitor_sum

    # 이전 이슈와 비교
    compare_result = compare_prev_issue(cloner_data, view_data, last_issue_body, total_cloner_sum, total_viewer_sum)
    prev_clone_dict = compare_result[0]
    prev_view_dict = compare_result[1]
    prev_total_clone = prev_clone_dict["today"]
    prev_total_view = prev_view_dict["today"]
    today_clone_status = get_status(prev_total_clone)
    today_view_status = get_status(prev_total_view)

    issue_clone_summary = '`The number of clones in two weeks.` <br/> \n'
    issue_view_summary = '`The number of view in two weeks.` <br/> \n'

    issue_cloner_header = f'## Unique Cloner 😊today : {total_cloner_sum} ({today_clone_status}{prev_total_clone}) <br/> \n'
    issue_viewer_header = f'## Unique viewer 😊today: {total_viewer_sum} ({today_view_status}{prev_total_view})<br/> \n'

    issue_list.append(issue_cloner_header)
    issue_list.append(issue_clone_summary)

    for unique_cloner in cloner_data:
        repo_name, cloner = unique_cloner
        cloner_update = prev_clone_dict[repo_name]
        today_clone = is_today(repo_name, today_unique_cloner)

        issue_list.append(
            f"- clone of [{repo_name}]({github_url}" + repo_name + f"): {cloner}  {cloner_update} {today_clone} \n")

    issue_list.append('<br/>' * 5)
    issue_list.append("\n")

    issue_list.append(issue_viewer_header)
    issue_list.append(issue_view_summary)

    for unique_view in view_data:
        repo_name, viewer = unique_view
        viewer_update = prev_view_dict[repo_name]
        today_view = is_today(repo_name, today_unique_viewer)
        issue_list.append(
            f"- view of [{repo_name}]({github_url}" + repo_name + f"): {viewer} {viewer_update} {today_view}\n")

    issue_list.append("If you, the creator, also visit or clone the repository daily, the results will be counted and "
                      "accumulated daily. Please be aware of this.<br/>")
    return ''.join(issue_list)


def get_status(value: int) -> str:
    if value > 0:
        return "🔼"
    elif value < 0:
        return "🔽"
    return "-"


def is_today(repository_name: str, data: dict):
    if repository_name in data:
        return f"/ today: {data[repository_name]}"
    return ""


def compare_prev_issue(current_cloner: list, current_view: list, last_issue: str, today_cloner: int,
                       today_viewer: int) -> list:
    print("last issue:", last_issue)
    prev_cloner = get_prev_cloner(last_issue)
    prev_viewer = get_prev_viewer(last_issue)
    cloner_compare = compare_prev_cloner(prev_cloner, current_cloner, today_cloner)
    viewer_compare = compare_prev_viewer(prev_viewer, current_view, today_viewer)
    return [cloner_compare, viewer_compare]


def get_prev_cloner(last_issue: str) -> dict:
    cloner_str = last_issue[:last_issue.find("Unique viewer")]
    prev_cloner_list = cloner_str.split('\n')
    prev_repo_info = {"sum": 0}
    for issue_info in prev_cloner_list:
        if issue_info.find('[') == -1:
            continue
        prev_repo_name = issue_info[issue_info.find('[') + 1:issue_info.find(']')]
        prev_clone_count = issue_info[issue_info.rfind(':') + 1:issue_info.rfind('(')]
        prev_repo_info[prev_repo_name] = int(prev_clone_count)
        prev_repo_info["sum"] += int(prev_clone_count)
    return prev_repo_info


def get_prev_viewer(last_issue: str) -> dict:
    cloner_str = last_issue[last_issue.find("Unique viewer") + 1:]
    prev_viewer_list = cloner_str.split('\n')
    prev_repo_info = {"sum": 0}
    for issue_info in prev_viewer_list:
        if issue_info.find('[') == -1:
            continue
        prev_repo_name = issue_info[issue_info.find('[') + 1:issue_info.find(']')]
        prev_viewer_count = issue_info[issue_info.rfind(':') + 1:issue_info.rfind('(')]
        prev_repo_info[prev_repo_name] = int(prev_viewer_count)
        prev_repo_info["sum"] += int(prev_viewer_count)
    return prev_repo_info


def compare_prev_cloner(prev_cloner: dict, current_cloner: list, today_clone_count: int) -> dict:
    compare_result = {}
    for repo_name, clone_count in current_cloner:
        today_cloner = clone_count - prev_cloner.get(repo_name, 0)
        if today_cloner > 0:
            cloner_status = "(🔼{})".format(today_cloner)
        elif today_cloner == 0:
            cloner_status = "(-)"
        else:
            cloner_status = "(🔽{})".format(today_cloner)

        if today_cloner == clone_count:
            cloner_status = "(🔅 new)"
        compare_result[repo_name] = cloner_status
    compare_result["today"] = today_clone_count - prev_cloner.get("sum", 0)
    return compare_result


def compare_prev_viewer(prev_viewer, current_viewer, today_viewer_count) -> dict:
    compare_result = {}
    for curr_cloner_data in current_viewer:
        curr_repo_name, curr_view_count = curr_cloner_data
        if curr_repo_name in prev_viewer:
            prev_count = prev_viewer[curr_repo_name]
            viewer_status = ""
            today_viewer = curr_view_count - prev_count
            if today_viewer > 0:
                viewer_status = "(🔼" + str(today_viewer) + ")"
            elif today_viewer == 0:
                viewer_status = "(-)"
            else:
                viewer_status = "(🔽" + str(today_viewer) + ")"
        else:
            viewer_status = "(🔅 new)"
        compare_result[curr_repo_name] = viewer_status
    compare_result["today"] = today_viewer_count - prev_viewer["sum"]
    return compare_result


# TODO prev_repositories 안에다가 넣기.
def get_last_issue_cloner(last_issue_body: str) -> PrevIssue:
    cloner_title, last_idx = get_last_issue_cloner_title(last_issue_body)
    cloner_summary, last_idx = get_last_issue_cloner_summary(last_issue_body, last_idx)
    cloner_body, last_idx = get_last_issue_cloner_body(last_issue_body, last_idx)
    prev_cloner = PrevIssue(cloner_title, cloner_summary)
    print(prev_cloner)


def get_last_issue_cloner_title(last_issue_body: str) -> tuple:
    cloner_title_idx = last_issue_body.find(CLONER_TITLE)
    cloner_title_last_idx = last_issue_body.find('\n', cloner_title_idx)
    return last_issue_body[cloner_title_idx:cloner_title_last_idx], cloner_title_last_idx


def get_last_issue_cloner_summary(last_issue_body: str, idx: int) -> tuple:
    cloner_summary_idx = last_issue_body.find('`', idx)
    cloner_summary_last_idx = last_issue_body.find('\n', cloner_summary_idx)
    return last_issue_body[cloner_summary_idx:cloner_summary_last_idx], cloner_summary_last_idx


def get_last_issue_cloner_body(last_issue_body: str, idx: int) -> tuple:
    cloner_body_idx = last_issue_body.find('-', idx)
    cloner_body_last_idx = last_issue_body.find('#', cloner_body_idx)
    return last_issue_body[cloner_body_idx:cloner_body_last_idx], cloner_body_last_idx