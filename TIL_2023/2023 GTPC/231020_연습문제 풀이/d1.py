def minimum_coupons_required(a, b):
    count = 0

    while a > b:
        # 쿠폰을 사용해서 가격을 할인
        a = (a // 2) + 100

        # 쿠폰 사용 횟수 증가
        count += 1

        # 가격이 더 이상 b 이하가 아니면 불가능
        if a <= b:
            return count

    return -1  # 불가능한 경우

a, b = map(int, input().split())  # 행렬의 크기 입력 받기

result = minimum_coupons_required(a, b)
print(result)
