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

lst_s = list(map(int, input().split(" ")))
lst_f = []
result = []

# 배가 2대일 경우
if i == 1 or i == 2:
    result = max(lst_s)
    print(result)

# 배가 3대일 경우
elif i == 3:
    result = sum(lst_s)
    print(result)

# 배가 4대일 경우 
elif i > 3:
    while True:
        # s -> f
        lst_s.sort()        # lst_s 리스트 정렬하기
        n, m = lst_s[0], lst_s[1]    # 가장 작은수 2개 선택
        del lst_s[:2]  # 가장 작은수 2개 제거
        lst_f.append(n)  # lst_s에서 가장 큰수 뽑아서 lst_f에 넣기
        lst_f.append(m)  # lst_s에서 가장 큰수 뽑아서 lst_f에 넣기
        result.append(m)  # 가장 큰수는 result에 저장
        # print(lst_s, lst_f, result)

        if len(lst_f) == i:
            break
        
        # f->s
        lst_f.sort()    # lst_f 정렬
        m = lst_f[0]    # 가장 작은수 선택    
        del lst_f[0]
        lst_s.append(m)  # 가장 작은값 뽑아서 lst_s에 넣기
        result.append(m)    # 가장 작은값 result에 넣기
        # print(lst_s, lst_f, result)
        

        # s -> f
        lst_s.sort()    # lst_s 정렬
        n, m = lst_s[-2], lst_s[-1]   # 가장 큰수 2개 뽑기
        del lst_s[-2:]  # 가장 큰 수 2개 제거
        lst_f.append(n)  # 가장 큰 수 2개 
        lst_f.append(m)  # 가장 큰 수 2개 
        result.append(m)  # 큰값 result에 담기
        # print(lst_s, lst_f, result)

        if len(lst_f) == i:
            break
        
        #f -> s
        lst_f.sort()    # lst_f 정렬
        to_s = lst_f[0]    # 가장 작은수 선택    
        del lst_f[0]    # 가장 작은수 제거
        lst_s.append(to_s)  # 가장 작은값 뽑아서 lst_s에 넣기
        result.append(to_s)    # 가장 작은값 result에 넣기
        # print(lst_s, lst_f)
        
    print(sum(result))
