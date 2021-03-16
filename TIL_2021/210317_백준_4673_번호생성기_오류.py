# 번호 생성기
def self_num(p_num):
    lst_num = list(str(p_num))
    result = int(p_num) + int(str(lst_num[0])) + int(str(lst_num[-1]))
    return result

# 초기 번호를 이용해서 10000보다 작은 수를 모두 생성
_init = 33
print(_init)
while True:
    a = self_num(_init)
    if a >= 10000:
        break
    print(a)
    _init = a

