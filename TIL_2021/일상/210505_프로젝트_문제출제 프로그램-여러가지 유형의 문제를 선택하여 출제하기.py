import random
dic_digit = {
    '1': [2, 9],
    '2': [10, 99],
    '3': [100, 999]
}

# 숫자 생성하기
def make_two_one(p_up, p_dn):
    test_num = 15
    lst_up = list([random.randint(dic_digit[p_up][0], dic_digit[p_up][1]) for i in range(test_num)])
    lst_dn = list([random.randint(dic_digit[p_dn][0], dic_digit[p_dn][1]) for i in range(test_num)])
    lst_div = list(['-----' for i in range(test_num)])
    lst_asw = list(lst_up[i] * lst_dn[i] for i in range(test_num))
    return lst_up, lst_dn, lst_div, lst_asw

# 문제지 만들기
def make_math_paper(p_up, p_dn):
    lst_up, lst_dn, lst_div, lst_asw = make_two_one(p_up, p_dn)
    quiz_file = open(f'{p_up}자리 수_{p_dn}자리 수 곱셈_문제지.txt', 'w')

    # 문제지 헤더 작성하기
    quiz_file.write((' ' * 10) + f'{p_up}자리 X {p_dn}자리 문제풀이 \n\n')
    quiz_file.write('+ __학년 ___반 이름 : _________\n\n+ 날짜 : __월 __일 ___요일\n\n')

    quiz_file.write('\n\n')

    for i in range(0, len(lst_up), 3):  # 총 문제에서 3문제씩
        str_count_format = '%s.%20s.%20s.\n'  # 문제번호 위치
        str_up_format = '%5s%22s%21s\n'  # 곱하기 위의 숫자 위치
        str_dn_format = '%s%4s%18s%4s%17s%4s\n'  # 곱하기와 아래 숫자 위치
        str_div_format = '%s%22s%21s\n'  # 구분자 위치
        quiz_file.write(str_count_format % (i+1, i+2, i+3))
        quiz_file.write(str_up_format % (lst_up[i], lst_up[i+1], lst_up[i+2]))
        quiz_file.write(str_dn_format %
                        ('X', lst_dn[i], 'X', lst_dn[i+1], 'X', lst_dn[i+2]))
        quiz_file.write(str_div_format %
                        (lst_div[i], lst_div[i+1], lst_div[i+2]))
        quiz_file.write('\n\n\n')

    quiz_file.write('\n' * 2)
    quiz_file.write('-' * 30 + ' 정 답 ' + '-' * 30 + '\n')
    for c, i in enumerate(lst_asw):
        quiz_file.write(f'{c+1}번. {i}  ')

    quiz_file.close()

up = input('곱셈식의 윗단 자리수를 입력하세요.( 1 / 2 / 3 ) : ')
dn = input('곱셈식의 아랫단 자리수를 입력하세요.( 1 / 2 / 3 ) : ')
make_math_paper(up, dn)