# 200516_TIL_html 태그
- a 태그 - 링크 연결
```
< a href = "1.html" target = "_blank">태그</1> # 탭을 열어서 링크 열기
```

- 팀버너스리 : 웹의 창시자
- html의 발전 과정
	- GML - SGML - SGMLauid - HTML
		- 기존태그 17개에 + a태그 추가
- 태그의 중첩 - 리스트의 그룹핑
	- 리스트 - li 태그
```
<li> 리스트 </li>
```

	- 리스트의 묶음 - ul / ol 태그
	- ul - 번호 없는 태그
	- ol - 번호를 달아서 목록 만들기 태그
- title 태그 - 브라우저의 탭에 제목으로 표시 만들기
	- 검색엔젠 최적화에서 중요하여 어떤 태그보다 우선 노출

- meta 태그 : 웹에 표시되지는 않지만, 컴퓨터가 인식되기 쉽도록 함.
	- meta태그는 닫는 태그는 따로 없음.
```
<meata charset = "utf-8"> #한글을 표시하도록 함.
<meata name="description" content="과학실험도구를 인공지능이 인식하여 명칭과 사용방법을 알려줍니다."> # 웹페이지의 정보를 간단히 나타냄
<meta name="keywords" content="과학실험도구, 인공지능, 실험도구설명, 실험도구사용방법">
```

* <!DOCTYPE html> 의미
	* Document Type Declaration 
	* 브라우저에게 문서의 형식을 알려줌. 
	* html5에서 선언
* 의미로서의 HTML - 시만텍 태그
	* header - 머리글 영역을 표시
	* nav - 네비게이션 영역을 알려줌
	* article - 본문영역을 표시
	* footer - 바닥글 영역을 표시
	* section - 같은 내용을 그룹을 지음
