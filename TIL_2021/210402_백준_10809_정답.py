# 입력받은 단어에 사용된 알파벳의 사용여부 및 위치 출력하기
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for i in alphabet:
    print(word.find(char(x)))   # char() : 숫자를 문자로 , ord() : 문자를 숫자로