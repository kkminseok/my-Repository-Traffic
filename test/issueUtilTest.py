import pytest
from pytest_mock import mocker, MockerFixture

from issueUtil import get_prev_cloner, compare_prev_issue


def test_compare_prev_issue(cloner: list, viewer: list, last_issue: str, mocker: MockerFixture):
    def get_prev_cloner(last_issue: str) -> dict:
        cloner_str = last_issue[:last_issue.find("Unique viewer")]
        prev_cloner_list = cloner_str.split('\n')
        prev_repo_info = {}
        for issue_info in prev_cloner_list:
            if issue_info.find('[') == -1:
                continue
            prev_repo_name = issue_info[issue_info.find('[') + 1:issue_info.find(']')]
            prev_clone_count = issue_info[issue_info.rfind(':') + 1:issue_info.rfind('<')]
            prev_repo_info[prev_repo_name] = int(prev_clone_count)
        return prev_repo_info

    def get_prev_viewer(last_issuer: str) -> dict:
        cloner_str = last_issue[last_issue.find("Unique viewer") + 1:]
        prev_viewer_list = cloner_str.split('\n')
        prev_repo_info = {}
        for issue_info in prev_viewer_list:
            if issue_info.find('[') == -1:
                continue
            prev_repo_name = issue_info[issue_info.find('[') + 1:issue_info.find(']')]
            prev_viewer_count = issue_info[issue_info.rfind(':') + 1:issue_info.rfind('<')]
            prev_repo_info[prev_repo_name] = int(prev_viewer_count)
        return prev_repo_info

    def compare_prev_cloner(prev, curr) -> dict:
        compare_result = {}
        for curr_cloner_data in curr:
            curr_repo_name, curr_clone_count = curr_cloner_data
            if curr_repo_name in prev:
                prev_count = prev[curr_repo_name]
                print("prev count:", prev_count, "current count:", curr_clone_count)
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
        return compare_result

    mocker.patch("issueUtil.get_prev_cloner", get_prev_cloner)
    mocker.patch("issueUtil.get_prev_viewer", get_prev_viewer)
    mocker.patch("issueUtil.compare_prev_cloner", compare_prev_cloner)
    # last_issue parsing
    compare_prev_issue(cloner, viewer, last_issue)
