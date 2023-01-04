def create_issue_content(cloner_data: list, view_data: list, last_issue_body: str) -> str:
    # 문자열 그냥 합치면 효율성이 떨이짐.
    github_url = 'https://github.com/'
    issue_list = []
    # 오늘까지의 총 cloner 수
    total_cloner_sum = today_cloner(cloner_data)
    total_view_sum = today_viewer(view_data)
    # 이전 이슈와 비교
    compare_result = compare_prev_issue(cloner_data, view_data, last_issue_body, total_cloner_sum, total_view_sum)
    prev_clone_dict = compare_result[0]
    prev_view_dict = compare_result[1]
    prev_total_clone = prev_clone_dict["today"]
    prev_total_view = prev_view_dict["today"]
    today_clone_status = get_status(prev_total_clone)
    today_view_status = get_status(prev_total_view)

    issue_cloner_header = f'## Unique Cloner 😊today : {total_cloner_sum} ({today_clone_status}{prev_total_clone}) <br/> \n'
    issue_viewer_header = f'## Unique viewer 😊today: {total_view_sum} ({today_view_status}{prev_total_view})<br/> \n'
    issue_list.append(issue_cloner_header)

    for unique_cloner in cloner_data:
        repo_name, cloner = unique_cloner
        cloner_update = prev_clone_dict[repo_name]
        issue_list.append(f"- [{repo_name}]({github_url}" + repo_name + f") 의 클론 수:{cloner}  {cloner_update} <br/>\n")

    issue_list.append('<br/>' * 5)
    issue_list.append("\n")

    issue_list.append(issue_viewer_header)

    for unique_view in view_data:
        repo_name, viewer = unique_view
        viewer_update = prev_view_dict[repo_name]
        issue_list.append(f"- [{repo_name}]({github_url}" + repo_name + f") 의 방문자:{viewer} {viewer_update} <br/>\n")

    issue_list.append("If you, the creator, also visit or clone the repository daily, the results will be counted and "
                      "accumulated daily. Please be aware of this.<br/>")

    return ''.join(issue_list)


def get_status(value: int) -> str:
    if value > 0:
        return "🔼"
    elif value < 0:
        return "🔽"
    return "-"


def today_cloner(today_cloner: list) -> int:
    clone_sum = 0
    for today_clone, val in today_cloner:
        clone_sum += val
    return clone_sum


def today_viewer(today_viewer: list) -> int:
    viewer_sum = 0
    for today_view, val in today_viewer:
        viewer_sum += val
    return viewer_sum


def compare_prev_issue(current_cloner: list, current_view: list, last_issue: str, today_cloner: int,
                       today_viewer: int) -> list:
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
        print(issue_info)
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


def compare_prev_cloner(prev_cloner, current_cloner, today_cloner) -> dict:
    compare_result = {}
    for curr_cloner_data in current_cloner:
        curr_repo_name, curr_clone_count = curr_cloner_data
        if curr_repo_name in prev_cloner:
            prev_count = prev_cloner[curr_repo_name]
            cloner_status = ""
            today_cloner = curr_clone_count - prev_count
            if today_cloner > 0:
                cloner_status = "(🔼" + str(today_cloner) + ")"
            elif today_cloner == 0:
                cloner_status = "(-)"
            else:
                cloner_status = "(🔽" + str(today_cloner) + ")"
        else:
            cloner_status = "(🔅 new)"
        compare_result[curr_repo_name] = cloner_status
    compare_result["today"] = prev_cloner["sum"] - today_cloner
    return compare_result


def compare_prev_viewer(prev_viewer, current_viewer, today_viewer) -> dict:
    compare_result = {}
    for curr_cloner_data in current_viewer:
        curr_repo_name, curr_view_count = curr_cloner_data
        if curr_repo_name in prev_viewer:
            prev_count = prev_viewer[curr_repo_name]
            viewer_status = ""
            today_cloner = curr_view_count - prev_count
            if today_cloner > 0:
                viewer_status = "(🔼" + str(today_cloner) + ")"
            elif today_cloner == 0:
                viewer_status = "(-)"
            else:
                viewer_status = "(🔽" + str(today_cloner) + ")"
        else:
            viewer_status = "(🔅 new)"
        compare_result[curr_repo_name] = viewer_status
    compare_result["today"] = prev_viewer["sum"] - today_viewer
    return compare_result
