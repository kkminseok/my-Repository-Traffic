import os

from gitUtils import get_all_repositories

if __name__ == "__main__":
    token = os.environ['MY_TRAFFIC_TOKEN']

    print(get_all_repositories(token))