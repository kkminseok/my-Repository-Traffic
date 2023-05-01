import re

from constant.constant import VIEWER_TITLE, CLONER_TODAY_SEPERATOR
from data_class.issue.prev_issue import PrevIssue


def get_last_issue_viewer(last_issue_body: str) -> PrevIssue:
    viewer_title, last_idx = get_last_issue_viewer_title(last_issue_body)
    viewer_summary, last_idx = get_last_issue_viewer_summary(last_issue_body, last_idx)
    viewer_body = get_last_issue_viewer_body(last_issue_body, last_idx)
    prev_viewer = PrevIssue(viewer_title, viewer_summary)
    return set_prev_issue_viewer(prev_viewer, viewer_body)


def get_last_issue_viewer_title(last_issue_body) -> tuple:
    viewer_title_idx = last_issue_body.find(VIEWER_TITLE)
    viewer_title_last_idx = last_issue_body.find('\n', viewer_title_idx)
    return last_issue_body[viewer_title_idx:viewer_title_last_idx], viewer_title_last_idx


def get_last_issue_viewer_summary(last_issue_body: str, idx: int) -> tuple:
    viewer_summary_idx = last_issue_body.find('`', idx)
    viewer_summary_last_idx = last_issue_body.find('\n', viewer_summary_idx)
    return last_issue_body[viewer_summary_idx:viewer_summary_last_idx], viewer_summary_last_idx


def get_last_issue_viewer_body(last_issue_body: str, idx: int) -> str:
    viewer_body_idx = last_issue_body.find('-', idx)
    return last_issue_body[viewer_body_idx:]


def set_prev_issue_viewer(prev_viewer: PrevIssue, body: str) -> PrevIssue:
    line = body.splitlines(True)
    for prev_repository_info in line:
        repository_name = get_repository_name(prev_repository_info)
        if repository_name == "":
            continue
        week_count = get_two_week_count(prev_repository_info)
        today_count = get_today_count(prev_repository_info)
        prev_viewer.add_prev_viewer_repository(repository_name, week_count, today_count)
    return prev_viewer


def get_repository_name(line: str) -> str:
    idx = line.find('[')
    if idx == -1:
        return ""
    return line[line.find('[') + 1:line.find(']')]


def get_two_week_count(line: str) -> int:
    idx = line.find(')')
    return int(re.sub(r'[^0-9]', '', line[idx:line.find('(', idx)]))


def get_today_count(line: str) -> int:
    idx = line.find(CLONER_TODAY_SEPERATOR)
    if idx == -1:
        return 0
    print(idx)
    print(line[idx])
    print(line)
    return int(re.sub(r'[^0-9]', '', line[idx:line.find('\n', idx)]))
    # return int(re.sub(r'[^0-9]', '', line[line.find('(', idx):line.find('\n', idx)]))
