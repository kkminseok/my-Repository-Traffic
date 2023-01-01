import pytest


def test_compare_prev_issue(cloner: list, viewer: list, last_issue: str):
    # last_issue parsing
    last_issue_list = last_issue.split('\n')
    prev_repo_info = {}
    for issue_info in last_issue_list:
        if issue_info.find('[') == -1:
            continue
        prev_repo_name = issue_info[issue_info.find('[')+1:issue_info.find(']')]
        prev_clone_count = issue_info[issue_info.rfind(':')+1:issue_info.rfind('<')]
        prev_repo_info[prev_repo_name] = int(prev_clone_count)

    for clone_data in cloner:
        curr_repo_name, curr_clone_count = clone_data
        print(curr_repo_name,curr_clone_count)
        if curr_repo_name in prev_repo_info:
            prev_count = prev_repo_info[curr_repo_name]
            today_cloner = curr_clone_count - prev_count
            if today_cloner > 0:
                print("(🔼" + str(today_cloner) + ")")
            elif today_cloner == 0:
                print("(-)")
            else:
                print("(🔽" + str(today_cloner) + ")")





