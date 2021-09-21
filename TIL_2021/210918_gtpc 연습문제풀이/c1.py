import math
n, m = input("팩토리얼 구할 숫자 입력하세요 : ").split()
a = int(n)
b = int(m)

# print(n, m)

# 두 수중에 큰 수가 n, 작은수는 m
n = max(int(a), int(b)) - 1
m = min(int(a), int(b)) - 1

# print(n, m)

result = math.factorial(n+m) / (math.factorial(m) * math.factorial(n))

print(int(result))