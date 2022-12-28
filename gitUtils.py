import string
from github import Github


def get_all_repositories(token: string):
    g = Github(token)
    repos = g.get_user().get_repos("public", "owner")
    return repos


def get_all_repositories_traffic(repos):
    traffic_dict = {}
    for repo in repos:
        contents = repo.get_clones_traffic()
        unique_cloner = contents['uniques']
        if unique_cloner == 0:
            continue
        traffic_dict[repo.full_name] = contents['uniques']
    return traffic_dict
