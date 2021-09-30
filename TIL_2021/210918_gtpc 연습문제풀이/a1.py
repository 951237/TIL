# 곱해야하는 숫자 구하기
n, m = map(int, input().split())
num_bread = n * m  # 구매해야하는 빵의 개수구하기

# 최소비용으로 빵 구매하기
if num_bread < 30:
    result = 9000
    print(result)
elif num_bread % 30 == 0:
    result = num_bread // 30 * 9000
    print(result)
elif num_bread < 50:
    result = 15000
    print(result)
elif num_bread % 50 == 0:
    result = num_bread // 50 * 15000
    print(result)
else:
    num_bread_spare = num_bread % 50
    _50 = num_bread // 50
    if num_bread_spare > 30:
        result = (_50 * 15000) + 18000
        print(result)
    else:
        result = (_50 * 15000) + 9000
        print(result)