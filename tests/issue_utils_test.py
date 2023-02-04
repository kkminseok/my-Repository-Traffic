from pytest_mock import MockerFixture

from module.issue_utils import compare_prev_issue, create_issue_content


def test_create_issue_content(cloner: list, viewer: list, last_issue: str, mocker: MockerFixture):
    mocker.patch("issue_utils.get_prev_cloner", get_prev_cloner)
    mocker.patch("issue_utils.get_prev_viewer", get_prev_viewer)
    mocker.patch("issue_utils.compare_prev_cloner", compare_prev_cloner)
    mocker.patch("issue_utils.today_cloner", today_cloner)
    result = create_issue_content(cloner, viewer, last_issue)
    print(result)


def today_cloner(today_cloner: list) -> int:
    clone_sum = 0
    for today_clone, val in today_cloner:
        clone_sum += val
    return clone_sum


def test_compare_prev_issue(cloner: list, viewer: list, last_issue: str, today_cloner: int, today_viewer: int,
                            mocker: MockerFixture):
    mocker.patch("issue_utils.get_prev_cloner", get_prev_cloner)
    mocker.patch("issue_utils.get_prev_viewer", get_prev_viewer)
    mocker.patch("issue_utils.compare_prev_cloner", compare_prev_cloner)
    mocker.patch("issue_utils.compare_prev_viewer", compare_prev_viewer)
    # last_issue parsing
    compare_prev_issue(cloner, viewer, last_issue, today_cloner, today_viewer)


def get_prev_cloner(last_issue: str) -> dict:
    cloner_str = last_issue[:last_issue.find("Unique viewer")]
    prev_cloner_list = cloner_str.split('\n')
    prev_repo_info = {"sum": 0}
    for issue_info in prev_cloner_list:
        if issue_info.find('[') == -1:
            continue
        prev_repo_name = issue_info[issue_info.find('[') + 1:issue_info.find(']')]
        prev_clone_count = issue_info[issue_info.rfind(':') + 1:issue_info.rfind('<')]
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
        prev_viewer_count = issue_info[issue_info.rfind(':') + 1:issue_info.rfind('<')]
        prev_repo_info[prev_repo_name] = int(prev_viewer_count)
        prev_repo_info["sum"] += int(prev_viewer_count)
    return prev_repo_info


def compare_prev_cloner(prev, curr, today_clone) -> dict:
    compare_result = {}
    for curr_cloner_data in curr:
        curr_repo_name, curr_clone_count = curr_cloner_data
        if curr_repo_name in prev:
            prev_count = prev[curr_repo_name]
            cloner_status = ""
            today_cloner = curr_clone_count - prev_count
            if today_cloner > 0:
                cloner_status = "(🔼" + str(today_cloner) + ")"
            elif today_cloner == 0:
                cloner_status = "(-)"
            else:
                cloner_status = "(🔽" + str(today_cloner) + ")"
        else:
            cloner_status = "new!!"
        compare_result[curr_repo_name] = cloner_status
    # 차이계산
    compare_result["today"] = today_clone - prev["sum"]
    return compare_result


def compare_prev_viewer(prev, curr, today_view) -> dict:
    compare_result = {}
    for curr_cloner_data in curr:
        curr_repo_name, curr_view_count = curr_cloner_data
        if curr_repo_name in prev:
            prev_count = prev[curr_repo_name]
            viewer_status = ""
            today_cloner = curr_view_count - prev_count
            if today_cloner > 0:
                viewer_status = "(🔼" + str(today_cloner) + ")"
            elif today_cloner == 0:
                viewer_status = "(-)"
            else:
                viewer_status = "(🔽" + str(today_cloner) + ")"
        else:
            viewer_status = "🔅 new"
        compare_result[curr_repo_name] = viewer_status
    # 차이계산
    compare_result["today"] = today_view - prev["sum"]
    return compare_result
