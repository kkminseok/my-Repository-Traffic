# my-Repository-Traffic
내 모든 레포지토리 하루 or 2주일간 트래픽을 볼 수 있는 git Action 스케줄러 작성

## 고려한 사항

- git API를 쓰려면 개인의 Token이 필요하고 안전하게 관리하는 방법이 있는가? -> git자체가 관리하는 git Action으로 작성하자.
- 사용자에게 결과를 웹으로 보여줘야하나? git Action으로 가능한가? -> 가능하다.
- 최선인가? 웹말고 간단하게 보여줄 수 있는 방법은? -> git Issue탭에 스케줄러로 보여준다.
- gitAction 트리거는 어떠한 걸 써야하지? -> workflow-dispatcher
- 사용언어는? -> 그래프 같은걸 그리기 쉬운 python을 채택. 
