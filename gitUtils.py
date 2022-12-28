import string
from github import Github


def get_all_repositories(token: string):
    g = Github(token)
    repo = g.get_repo("PyGithub/PyGithub")
    contents = repo.get_top_paths()
    print(contents)
