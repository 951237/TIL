c = 0
def f(x, y):
    global n, m, c
    if x == n and y == m:  # 도착했을 때문 길을 1개로 인정
        c += 1
        return c
    if x > n or y > m:
        return
    f(x+1, y)
    f(x, y+1)
    return c

n, m = map(int, input().split())
c = f(1,1)
print(c)