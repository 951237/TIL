n = int(input())
# 입력값을 리스트로 받기
lst = list(map(float, input().split()))
t = float(input())

for i in range(n):
    if i == 0:
        min = abs(t-lst[i])
    k = abs(t - lst[i])
    if k < min:
        min = k
        result = lst[i]
        
print("{:.2f}".format(result))