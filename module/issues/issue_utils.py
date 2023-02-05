from data_class.issue.prev_issue import PrevIssue
from data_class.repositories.cloner_repositories import ClonerRepositories
from data_class.repositories.cloner_repository import ClonerRepository
from data_class.repositories.visitor_repositories import VisitorRepositories
from data_class.repositories.visitor_repository import VisitorRepository
from module.issues.prev_issue_cloner_utils import get_last_issue_cloner
from module.issues.prev_issue_viewer_utils import get_last_issue_viewer


def separate_issue(last_issue_body: str) -> tuple:
    prev_issue_cloner = get_last_issue_cloner(last_issue_body)
    prev_issue_viewer = get_last_issue_viewer(last_issue_body)
    return prev_issue_cloner, prev_issue_viewer


def create_issue_content(prev_issue_cloner: PrevIssue, prev_issue_visitor: PrevIssue, token: str) -> str:
    # 문자열 그냥 합치면 효율성이 떨이짐.
    issue_list: list = []
    github_url: str = 'https://github.com/'
    cloner_data: dict = ClonerRepositories.instance().repositories
    view_data: dict = VisitorRepositories.instance().repositories
    total_cloner_sum: int = ClonerRepositories.instance().cloner_sum
    total_viewer_sum: int = VisitorRepositories.instance().visitor_sum

    # 이전 이슈와 비교
    cloner_diff = total_cloner_sum - prev_issue_cloner.title_count
    viewer_diff = total_viewer_sum - prev_issue_visitor.title_count
    today_clone_status = get_status(cloner_diff)
    today_view_status = get_status(viewer_diff)

    issue_cloner_header = f'## Unique Cloner 😊today : {total_cloner_sum} ({today_clone_status}{cloner_diff})<br/>\n'
    issue_viewer_header = f'## Unique viewer 😊today: {total_viewer_sum} ({today_view_status}{viewer_diff})<br/>\n'
    issue_clone_summary = '`The number of clones in two weeks.` <br/> \n'
    issue_view_summary = '`The number of view in two weeks.` <br/> \n'

    issue_list.append(issue_cloner_header)
    issue_list.append(issue_clone_summary)

    for full_name, unique_cloner in cloner_data.items():
        clone_diff_result = compare_prev_cloner(full_name, prev_issue_cloner.prev_repositories, unique_cloner)
        issue_list.append(
            f"- clone of [{full_name}]({github_url}" + full_name + f"): {unique_cloner.cloner_count} {clone_diff_result} \n")

    issue_list.append('<br/>' * 5)
    issue_list.append("\n")

    issue_list.append(issue_viewer_header)
    issue_list.append(issue_view_summary)

    for full_name, unique_viewer in view_data.items():
        visitor_diff_result = compare_prev_viewer(full_name, prev_issue_visitor.prev_repositories, unique_viewer)
        issue_list.append(
            f"- view of [{full_name}]({github_url}" + full_name + f"): {unique_viewer.visitor_count} {visitor_diff_result}\n")

    issue_list.append("If you, the creator, also visit or clone the repository daily, the results will be counted and "
                      "accumulated daily. Please be aware of this.<br/>")
    return ''.join(issue_list)


def get_status(value: int) -> str:
    if value > 0:
        return "🔼"
    elif value < 0:
        return "🔽"
    return "-"


def compare_prev_cloner(full_name: str, prev_cloner_repositories: dict, curr_cloner_info: ClonerRepository) -> str:
    compare_result = []
    if full_name in prev_cloner_repositories:
        two_week_cloner_diff = curr_cloner_info.cloner_count - prev_cloner_repositories[full_name].cloner_count
        if two_week_cloner_diff > 0:
            compare_result.append("(🔼{})".format(two_week_cloner_diff))
        elif two_week_cloner_diff < 0:
            compare_result.append("(🔽{})".format(two_week_cloner_diff))
        else:
            compare_result.append("(-)")
        if curr_cloner_info.today_cloner != 0:
            today_cloner_diff = curr_cloner_info.today_cloner - prev_cloner_repositories[full_name].today_cloner
            compare_result.append(f"/ today: {curr_cloner_info.today_cloner} ")
            if today_cloner_diff > 0:
                compare_result.append("(🔼{})".format(today_cloner_diff))
            elif today_cloner_diff < 0:
                compare_result.append("(🔽{})".format(today_cloner_diff))
    else:
        compare_result.append("(🔅 new)")
    return ''.join(compare_result)


def compare_prev_viewer(full_name: str, prev_viewer_repositories: dict, curr_viewer_info: VisitorRepository) -> str:
    compare_result = []
    if full_name in prev_viewer_repositories:
        two_week_viewer_diff = curr_viewer_info.visitor_count - prev_viewer_repositories[full_name].visitor_count
        if two_week_viewer_diff > 0:
            compare_result.append("(🔼{})".format(two_week_viewer_diff))
        elif two_week_viewer_diff < 0:
            compare_result.append("(🔽{})".format(two_week_viewer_diff))
        else:
            compare_result.append("(-)")
        if curr_viewer_info.today_visitor != 0:
            today_viewer_diff = curr_viewer_info.today_visitor - prev_viewer_repositories[full_name].today_visitor
            compare_result.append(f"/ today: {curr_viewer_info.today_visitor} ")
            if today_viewer_diff > 0:
                compare_result.append("(🔼{})".format(today_viewer_diff))
            elif today_viewer_diff < 0:
                compare_result.append("(🔽{})".format(today_viewer_diff))
    else:
        compare_result.append("(🔅 new)")
    return ''.join(compare_result)
