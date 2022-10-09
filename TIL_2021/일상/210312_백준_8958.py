N = int(input()) # 입력횟수 입력받기
for _ in range(N):
    _input = list(input())  # 입력받은 값을 리스트로 저장
    sum = 0
    cnt = 0
    for i in _input:
        # i가 0일경우는 1씩 올라가도록 카운트
        if i == 'O':
            cnt += 1
        # x가 나올경우 카운트 값을 초기화
        else:
            cnt = 0
        # 점수를 누계
        sum += cnt
    print(sum)