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
    return "## Unique Cloner <br/>\n\
- [kkminseok/my-Repository-Traffic](https://github.com/kkminseok/my-Repository-Traffic) 의 클론 수:18 <br/>\n\
- [kkminseok/Book](https://github.com/kkminseok/Book) 의 클론 수:15 <br/>\n\
- [kkminseok/real-world-springboot-vue.js](https://github.com/kkminseok/real-world-springboot-vue.js) 의 클론 수:13 <br/>\n\
- [kkminseok/Algorithm_solution](https://github.com/kkminseok/Algorithm_solution) 의 클론 수:9 <br/>\n\
- [kkminseok/5_kyh_spring_db_1](https://github.com/kkminseok/5_kyh_spring_db_1) 의 클론 수:4 <br/>\n\
- [kkminseok/kkminseok.github.io](https://github.com/kkminseok/kkminseok.github.io) 의 클론 수:3 <br/>\n\
- [kkminseok/JavaVersionDoc](https://github.com/kkminseok/JavaVersionDoc) 의 클론 수:2 <br/>\n\
- [kkminseok/SPA_VUE_Spring_Example](https://github.com/kkminseok/SPA_VUE_Spring_Example) 의 클론 수:2 <br/>\n\
- [kkminseok/Springkyh](https://github.com/kkminseok/Springkyh) 의 클론 수:2 <br/>\n\
- [kkminseok/todolist_book](https://github.com/kkminseok/todolist_book) 의 클론 수:2 <br/>\n\
- [kkminseok/2015110473_OpSc](https://github.com/kkminseok/2015110473_OpSc) 의 클론 수:1 <br/>\n\
- [kkminseok/2020_capstone_project_human_to_animal](https://github.com/kkminseok/2020_capstone_project_human_to_animal) 의 클론 수:1 <br/>\n\
- [kkminseok/2020_kotlin_deepleaning](https://github.com/kkminseok/2020_kotlin_deepleaning) 의 클론 수:1 <br/>\n\
- [kkminseok/4_kyh_spring_mvc_note](https://github.com/kkminseok/4_kyh_spring_mvc_note) 의 클론 수:1 <br/>\n\
- [kkminseok/binance_NFT](https://github.com/kkminseok/binance_NFT) 의 클론 수:1 <br/>\n\
- [kkminseok/js_study](https://github.com/kkminseok/js_study) 의 클론 수:1 <br/>\n\
- [kkminseok/leetcode](https://github.com/kkminseok/leetcode) 의 클론 수:1 <br/>\n\
- [kkminseok/OS_md](https://github.com/kkminseok/OS_md) 의 클론 수:1 <br/>\n\
- [kkminseok/springCICD_Practice](https://github.com/kkminseok/springCICD_Practice) 의 클론 수:1 <br/>\n\
<br/><br/><br/><br/><br/>\n\
## Unique viewer <br/> \n\
- [kkminseok/real-world-springboot-vue.js](https://github.com/kkminseok/real-world-springboot-vue.js) 의 방문자:27 <br/>\n\
- [kkminseok/Book](https://github.com/kkminseok/Book) 의 방문자:5 <br/>\n\
- [kkminseok/kkminseok.github.io](https://github.com/kkminseok/kkminseok.github.io) 의 방문자:3 <br/>\n\
- [kkminseok/4_kyh_spring_mvc_note](https://github.com/kkminseok/4_kyh_spring_mvc_note) 의 방문자:2 <br/>\n\
- [kkminseok/binance_NFT](https://github.com/kkminseok/binance_NFT) 의 방문자:2 <br/>\n\
- [kkminseok/JavaVersionDoc](https://github.com/kkminseok/JavaVersionDoc) 의 방문자:2 <br/>\n\
- [kkminseok/my-Repository-Traffic](https://github.com/kkminseok/my-Repository-Traffic) 의 방문자:2 <br/>\n\
- [kkminseok/TIL_Interview](https://github.com/kkminseok/TIL_Interview) 의 방문자:2 <br/>\n\
- [kkminseok/2020_Ec2_openAPI_project](https://github.com/kkminseok/2020_Ec2_openAPI_project) 의 방문자:1 <br/>\n\
- [kkminseok/Algorithm_solution](https://github.com/kkminseok/Algorithm_solution) 의 방문자:1 <br/>\n\
- [kkminseok/jekyll-theme-chirpy](https://github.com/kkminseok/jekyll-theme-chirpy) 의 방문자:1 <br/>\n\
- [kkminseok/kafka_message_example](https://github.com/kkminseok/kafka_message_example) 의 방문자:1 <br/>\n\
- [kkminseok/kkminseok](https://github.com/kkminseok/kkminseok) 의 방문자:1 <br/>\n\
"


