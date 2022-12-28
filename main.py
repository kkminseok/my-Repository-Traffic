import os

from gitUtils import get_all_repositories,get_all_repositories_traffic

if __name__ == "__main__":
    token = os.environ['MY_TRAFFIC_TOKEN']
    repos = get_all_repositories(token)
    traffic_of_all_repositories = get_all_repositories_traffic(repos)
    print(traffic_of_all_repositories)
