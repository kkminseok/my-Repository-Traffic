import string
from github import Github


def get_all_repositories(token: string):
    g = Github(token)
    return g.get_user().get_repos()
