import os

import gitUtils

if __name__ == "__main__":
    token = os.environ['MY_TRAFFIC_TOKEN']

    print(gitUtils.get_all_repositories(token))