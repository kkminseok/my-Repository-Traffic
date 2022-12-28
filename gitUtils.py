import string
from github import Github


def get_all_repositories(token: string):
    g = Github(token)
    repos = g.get_repos(20,"all")
    for repo in repos:
        print(repo)
        g.get_repo(repo.name)
        contents = repo.get_top_paths()
        print(contents)
