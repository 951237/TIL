# 몬드리안의 고민

'''
# 알고리즘
- 칸수 입력 받기
- 칸의 면적 입력 리스트로 받기
- 물감의 가격 입력 리스트로받기
- 면적 리스트 소팅 차례로
- 물감 리스트 소팅 - 반대로
- 리스트끼리 곱하기의 합

# 출력양식
- 최대비용
- 알파벳순()

#todo : 영어 리스트 출력
'''

# 입력 받기
i = int(input())

lst_rct = list(map(int, input().split(" ")))
lst_price = list(map(int, input().split(" ")))

# 리스트 정렬
lst_rct.sort()
lst_price.sort()

# 리스트간의 곱
result = [x * y for x, y in zip(lst_rct, lst_price)]

# 리시트의 합 출력
print(sum(result))