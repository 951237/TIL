# 알고리즘
'''
s → f : 가장 작은 두수 뽑기
f → s : 가장 작은 수 1개
s → f : 가장 큰수 2개
f → s : 가장 작은 수 1개

위의 4단계가 반복
'''

# 입력 받기
i = int(input())

lst_s = list(input().split(" "))
lst_f = []
result = []

# 배가 1대일경우
if i == 1:
    result = i

# 배가 2대일 경우
if i == 2:
    result = max(lst_s)

# 배가 3대일 경우
if i == 3:
    result = sum(lst_s)

# 재가 4대일 경우 
if i > 3:
    # lst_s 리스트 정렬하기
    # lst_s에서 가장 큰수 뽑아서 lst_f에 넣기
    # 가장 큰수는 result에 저장
    # lst_f 정렬, 가장 작은값 뽑아서 lst_s에 넣기, result에 넣기
    # lst_s 정렬, 가장 큰수 2개 뽑기
    # 큰값 result에 담기
    # lst_f 정렬, 가장 작은값 뽑아서 lst_s에 넣기, result에 넣기
    # 처음단계부터 반복
    

