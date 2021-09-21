import math
n, m = input("팩토리얼 구할 숫자 입력하세요 : ").split()
n = int(n)
m = int(m)

print(n, m)

result = math.factorial(n+1) / (math.factorial(m-1) * math.factorial(n-1))

print(int(result))