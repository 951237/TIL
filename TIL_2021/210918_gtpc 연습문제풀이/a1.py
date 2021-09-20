# 곱해야하는 숫자 구하기
n, m = input("팀수와 인원을 입력하시오. : ").split(" ")
num_bread = int(n) * int(m)
print(num_bread)
cnt = num_bread // 50 + 1  # 몫구하기

# 경우의 수와 가격 구하기
_min = 1000000000000000000000000000000000000000000
a, b = 0, 0
for i in range(cnt+1):
    temp = 50 * (cnt - i) + 30 * (i)
#     print(temp)
    if temp < num_bread:
        continue
    if temp < _min:
        _min = temp
        a, b = (cnt - i), i
price = 15000 * a + 9000 * b
print(price)
