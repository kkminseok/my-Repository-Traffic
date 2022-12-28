import string
from github import Github


def get_all_repositories(token: string):
    g = Github(token)
    repos = g.get_user().get_repos("owner")
    print(repos)
    for repo in repos:
        print(repo)
        contents = repo.get_clones_traffic()
        print(contents)
