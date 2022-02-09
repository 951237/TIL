import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe
# ^ (^de) : 문자열의 시작 > desk, destination
# $ (se$) : 문자열의 끝 > case, base

def print_match(p_input):
    m = p.match(p_input)    # 주어진 문자열과 처음부터 일치하는지 확인
    if m:
        print(m.group())    #
    else:
        print("매칭 되지 않음")

while True:
    m = input("단어를 입력하세요 : ")
    if m == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        print_match(m)

# 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") # 주어진 문자열과 처음부터 일치하는지 비교
# 3. m = p.search("비교할 문자열") # 주어진 문자열중에 일치하는게 있는지 확인
# 4. lst = p.findall("") # 일치하는 모든 것을 '리스트'형태로 반환