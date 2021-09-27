def hap(a):
    if a < 10:
        return a
    return hap(a//10)+a%10

k, n = map(int, input().split())

a, cnt = 1, 0

while(cnt < n):
    if hap(a) == k:
        cnt += 1
    a += 1
print(a-1)