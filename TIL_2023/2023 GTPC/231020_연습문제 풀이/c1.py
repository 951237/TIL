def round_division(a, b, k):
    # 나눗셈을 수행하고 결과를 소수점 아래 k+1 자리까지 계산
    result = a / b

    # 반올림을 수행하여 소수점 아래 k 자리까지 출력
    n = round(result, k)
    formatted_result = "{:.{k}f}".format(n, k=k)  # 결과값을 k 자리까지 출력
    return formatted_result

a, b, k = map(int, input().split())  # 행렬의 크기 입력 받기

result = round_division(a, b, k)

print(result)
