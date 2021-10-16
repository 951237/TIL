import math
t = int(input())
s = input()

if t == 1:
    print(0)
elif t == 2:
    print(1)
else:
    result = (math.factorial(t) - math.factorial(t-1)) / 2
    print(int(result))
