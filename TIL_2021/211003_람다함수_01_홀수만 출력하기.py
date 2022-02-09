# 홀수만 출력하기

lst_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 1, lst_num))