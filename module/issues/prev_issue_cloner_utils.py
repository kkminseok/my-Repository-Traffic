import re

from constant.constant import CLONER_TITLE, CLONER_TODAY_SEPERATOR
from data_class.issue.prev_issue import PrevIssue


def get_last_issue_cloner(last_issue_body: str) -> PrevIssue:
    cloner_title, last_idx = get_last_issue_cloner_title(last_issue_body)
    cloner_summary, last_idx = get_last_issue_cloner_summary(last_issue_body, last_idx)
    cloner_body, last_idx = get_last_issue_cloner_body(last_issue_body, last_idx)
    prev_cloner = PrevIssue(cloner_title, cloner_summary)
    return set_prev_issue_cloner(prev_cloner, cloner_body)


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


def set_prev_issue_cloner(prev_cloner: PrevIssue, body: str) -> PrevIssue:
    line = body.splitlines(True)
    for prev_repository_info in line:
        repository_name = get_repository_name(prev_repository_info)
        if repository_name == "":
            continue
        week_count = get_two_week_count(prev_repository_info)
        today_count = get_today_count(prev_repository_info)
        prev_cloner.add_prev_cloner_repository(repository_name, week_count, today_count)
    return prev_cloner


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
    return int(re.sub(r'[^0-9]', '', line[idx:line.find('\n', idx)]))
