def virus(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 3
    return 1 + virus(n-2) + virus(n-2) + virus(n-3) 

a, b = map(int, input().split())
print(a*virus(b))