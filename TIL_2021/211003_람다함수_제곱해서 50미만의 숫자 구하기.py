lst_num = [i for i in range(100)]  # 1부터 100까지의 숫자

# 제곱해서 50미만의 수
result = list(filter(lambda x: x*x < 50 ,lst_num))

print(result)