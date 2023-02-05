from typing import List, Dict
from unittest.mock import MagicMock

import github
import pytest_asyncio


@pytest_asyncio.fixture
async def cloner() -> list:
    return [('kkminseok/my-Repository-Traffic', 28), ('kkminseok/Book', 15),
            ('kkminseok/real-world-springboot-vue.js', 13), ('kkminseok/Algorithm_solution', 9),
            ('kkminseok/5_kyh_spring_db_1', 4), ('kkminseok/kkminseok.github.io', 3), ('kkminseok/JavaVersionDoc', 2),
            ('kkminseok/SPA_VUE_Spring_Example', 2), ('kkminseok/Springkyh', 2), ('kkminseok/2015110473_OpSc', 1),
            ('kkminseok/2020_capstone_project_human_to_animal', 1), ('kkminseok/2020_kotlin_deepleaning', 1),
            ('kkminseok/4_kyh_spring_mvc_note', 1), ('kkminseok/binance_NFT', 1), ('kkminseok/js_study', 1),
            ('kkminseok/leetcode', 1), ('kkminseok/OS_md', 1), ('kkminseok/springCICD_Practice', 1),
            ('kkminseok/todolist_book', 1)]


@pytest_asyncio.fixture
async def viewer() -> list:
    return [('kkminseok/real-world-springboot-vue.js', 27), ('kkminseok/Book', 5), ('kkminseok/kkminseok.github.io', 3),
            ('kkminseok/binance_NFT', 2), ('kkminseok/JavaVersionDoc', 2), ('kkminseok/my-Repository-Traffic', 2),
            ('kkminseok/TIL_Interview', 2), ('kkminseok/2020_Ec2_openAPI_project', 1),
            ('kkminseok/4_kyh_spring_mvc_note', 1), ('kkminseok/Algorithm_solution', 1),
            ('kkminseok/jekyll-theme-chirpy', 1), ('kkminseok/kafka_message_example', 1), ('kkminseok/kkminseok', 1)]


@pytest_asyncio.fixture
async def last_issue() -> str:
    return '## Unique Cloner 😊today : 51 (🔽-26) <br/>\n' \
           '`The number of clones in two weeks.` <br/>\n' \
           '- clone of [kkminseok/my-Repository-Traffic](https://github.com/kkminseok/my-Repository-Traffic): 17  (🔽-6) / today: 2\n' \
           '- clone of [kkminseok/2017_Alram_project](https://github.com/kkminseok/2017_Alram_project): 3  (-)\n' \
           '## Unique viewer 😊today: 111 (🔽-27)<br/>\n' \
           '`The number of view in two weeks.` <br/>\n' \
           '- view of [kkminseok/real-world-springboot-vue.js](https://github.com/kkminseok/real-world-springboot-vue.js): 74 (🔽-6)\n' \
           '- view of [kkminseok/4_kyh_spring_mvc_note](https://github.com/kkminseok/4_kyh_spring_mvc_note): 9 (🔼1) / today: 1\n'


@pytest_asyncio.fixture
async def today_cloner() -> int:
    return 100


@pytest_asyncio.fixture
async def today_viewer() -> int:
    return 100


@pytest_asyncio.fixture
async def token() -> str:
    return 'abcdeftoken1234'


@pytest_asyncio.fixture
async def repositories() -> github.PaginatedList.PaginatedList:
    class Repository:
        def __init__(self, full_name):
            self.full_name = full_name

    mock_paginated_list = MagicMock(spec=github.PaginatedList.PaginatedList)
    mock_paginated_list.__iter__.return_value = iter([
        Repository(full_name="kkminseok.repo1"),
        Repository(full_name="kkminseok.repo2"),
        Repository(full_name="kkminseok.repo3"),
    ])
    return mock_paginated_list
