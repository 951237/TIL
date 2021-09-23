# 곱해야하는 숫자 구하기
n, m = map(int, input("팀수와 인원을 입력하시오. : ").split(" "))
k = ((n*m+9) // 10)

if k <= 3:
    print("9000")
elif k <= 5:
    print("15000")
elif k==6:
    print("18000")
elif k==7:
    print("24000")
else:
    print("%d" %(k*3000))

