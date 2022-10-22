a, b, k = map(int, input().split())  # 행렬의 크기 입력 받기
n = a/b
n_round = round(n,k)
print(f'%.{k}f'%n_round)