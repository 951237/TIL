from random import *

words = ["apple", "banana", "orange"]  # 문제 단어들
word = choice(words)  # 단어들을 랜덤으로 선택하기
print("answer : " + word)  # 출력문
letters = ""  # 입력한 알파벳을 저장하는 변수

while True:  # 성공할 때까지 계속 반복
    succeed = True  # 성공변수 일단
    print()  # 한칸 띄기
    for w in word:  # 선택한 단어를 한글자씩 뿌려줌.
        if w in letters:  # 단어의 글자가 입력받은 변수에 있으면
            print(w, end=" ")  # 글자를 출력하고 한칸 띄워줌.
        else:  # 그렇지 않은 경우에는 처음에는 무조건 else구문을 수행
            print("_", end=" ")  # 단어의 수만큼 _를 출력
            succeed = False  # 성공변수를 False로 전환
    print()  # 한줄띄기

    if succeed:  # 만약 성공이면
        print("succeed")  # 메세지 출력
        break  # 반복문 탈출

    letter = input("Input letter > ")  # 단어의 입력을 받음.
    if letter not in letters:  # 입력받은 문자중에 알파벳이 없으면
        letters += letter  # 단어들을 계속적으로 누가기록.

    if letter in word:  # 단어에 알파벳이 있으면
        print("correct")  # 메세지 출력
    else:  # 그렇지 않다면
        print("wrong")  # 메세지 출력
