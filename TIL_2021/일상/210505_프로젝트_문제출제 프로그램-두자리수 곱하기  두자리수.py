# 두자리수 * 한자리 문제 출제 폼 바꾸기
import random
test_num = 15
lst_up = list([random.randint(10, 99) for i in range(test_num)])
lst_dn = list([random.randint(10, 99) for i in range(test_num)])
lst_div = list(['-----' for i in range(test_num)])
lst_asw = list(lst_up[i] * lst_dn[i] for i in range(len(lst_up)))

# todo : 문제지 파일 작성하기
quiz_file = open('두자리수_두자리수 곱셈_문제지.txt', 'w')

# 문제지 헤더 작성하기
quiz_file.write((' ' * 10) + '두 자리수 X 한자리 수 문제풀이 \n\n')
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
    quiz_file.write(str_div_format % (lst_div[i], lst_div[i+1], lst_div[i+2]))
    quiz_file.write('\n\n\n')

quiz_file.write('\n' * 2)
quiz_file.write('-' * 30 + ' 정 답 ' + '-' * 30 + '\n')
for c, i in enumerate(lst_asw):
    quiz_file.write(f'{c+1}번. {i}  ')

quiz_file.close()
