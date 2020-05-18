# 200518_TIL_html 5 
* input형식의 추가
	* date, month, range, search, url, email
* input의 속성
```
<form action = "post", autocomplete="on" # 자동완성 기능>
	<input type="password" name="passowrd" acutocomplete="auto"> # 자동완성기능은 form전체 혹은 개개별로 지정가능 
```
	* placeholder : 입력란에 안내 메세지 
	* autofocus : 페이지에 이동했을 때 원하는 입력칸에 커서 위치
* 입력값 체크 : 유효성 검사
```
<form action="post" required>
	<input type="text" pattern="[a-zA-Z'].+[0-9]
</form> 
```
	* required : 필수입력, 디폴트값은 그냥 제출
	*  pattern=“정규표현식” : 입력값을 받았을 경우 특정 문구로 입력을 강제함
		* 예시
			* [a-zA-Z] : 문자입력으로 강제
			* “.” : 어떤 문자든 상관없음
			* “+” : 어떤 문자든 1개이상 반드시 입력
			* [0-9] : 숫자로만 입력

#코딩/TIL