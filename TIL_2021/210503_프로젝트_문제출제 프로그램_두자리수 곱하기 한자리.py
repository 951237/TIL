# 두자리수 * 한자리 문제 출제 폼 바꾸기
import random
lst_up = list([random.randint(10, 99) for i in range(10)])
lst_dn = list([random.randint(2, 9) for i in range(10)])
lst_div = list(['-----' for i in range(10)])
lst_asw = list(lst_up[i] * lst_dn[i] for i in range(len(lst_up)))

# todo : 문제지 파일 작성하기
quiz_file = open('두자리수_한자리수 곱셈_문제지.txt', 'w')
answer_file = open('두자리수_한자리수 곱셈_답안지.txt', 'w')

# 문제지 헤더 작성하기
quiz_file.write('__학년 ___반 이름 : _________\n\n날짜 : __월 __일 ___요일\n\n')
quiz_file.write((' ' * 10) + '두 자리수 곱하기 한자리수 문제풀이')
quiz_file.write('\n\n')

for i in range(0, len(lst_up), 2):
    str_count_format = '%10s.%28s.\n'
    str_up_format = '%15s%30s\n'
    str_dn_format = '%10s%5s%27s  %s\n'
    str_div_format = '%15s%30s\n'
    quiz_file.write(str_count_format % (i+1, i+2))
    quiz_file.write(str_up_format % (lst_up[i], lst_up[i+1]))
    quiz_file.write(str_dn_format % ('X', lst_dn[i], 'X', lst_dn[i+1]))
    quiz_file.write(str_div_format % (lst_div[i], lst_div[i+1]))
    quiz_file.write('\n\n\n')

for t, i in enumerate(lst_asw):
    answer_file.write(f'{t+1}번. {i}\n\n')

quiz_file.close()
answer_file.close()
