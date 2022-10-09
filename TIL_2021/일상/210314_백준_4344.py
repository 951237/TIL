N = int(input())

for _ in range(N):
    # 입력받은 값을 분할해서 숫자로 바꿔서 리스트로 저장하기
    _input = list(map(int, input().split()))

    avg = 0
    _sum = 0

    for i in range(1, len(_input)):
        # 2번째 수를 모두 더하여 합을 구하기
        _sum += _input[i]
    avg = _sum / _input[0]

    # 리스트의 값을 평균값과 비교해서 높은 인원을 카운트하기
    cnt = 0
    for i in range(1, len(_input)):
        if _input[i] > avg:
            cnt += 1
    result = cnt/_input[0]*100
    # 소수점 3자리로 출력하도록 형식 정하기 
    print("{:.3f}%".format(round(result, 3)))

