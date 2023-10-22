def make_burgers(n, m):
    # 햄버거 패티 수 초기화
    patties = 0
    
    while n >= 2 and m >= 1:
        # 햄버거 패티를 만들어서 재료를 사용
        n -= 2
        m -= 1
        patties += 1
    
    return patties

n, m = map(int, input().split())  # 행렬의 크기 입력 받기

result = make_burgers(n, m)
print(result)
