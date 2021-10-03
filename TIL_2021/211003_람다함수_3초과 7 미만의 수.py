lst_num = [i for i in range(1, 101)]  # 1부터 100까지 

# 3이상 7미만 수 출력하기
result = list(filter(lambda x: 3 < x < 7 , lst_num))

print(result)