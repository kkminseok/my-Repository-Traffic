import os
from dotenv import load_dotenv


def get_token() -> str:
    load_dotenv()
    return os.environ['MY_TRAFFIC_TOKEN']