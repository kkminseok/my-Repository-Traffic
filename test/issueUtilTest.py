import pytest
import string


def test_compare_prev_issue(cloner: list, viewer: list, last_issue: str):
    # last_issue parsing
    last_issue_list = last_issue.split('\n')
    for issue_info in last_issue_list:
        if issue_info.find('[') == -1:
            continue
        repo_name = issue_info[issue_info.find('[')+1:issue_info.find(']')]
        print(repo_name)

    for clone_data in cloner:
        repo_name, clone_count = clone_data
        print(repo_name,clone_count)



