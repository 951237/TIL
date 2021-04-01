# 입력받은 단어에 사용된 알파벳의 사용여부 및 위치 출력하기
S = input()
alphabet = "abcdefghijklmnopqrstuqwz"    
result = []
for i in alphabet:
    if i in S:  # 알파벳이 입력단어에 들어 있으면
        k = S.find(i)  # 입력단어에서 글자의 위치를 찾기
        result.append(str(k))
    else:
        result.append('-1')
print(' '.join(result))  # 리스트를 ' '으로 분리하여 출력하기