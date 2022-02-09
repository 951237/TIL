#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#개요
'''
- 목표 : 게시물의 총건수와 한페이지에 보여줄 게시물을 입력했을 때 총페이지수를 리턴
- 문제점
    -
'''

#알고리즘
'''
1. 입력받기 : 총건수(m), 게시물(n) / 단, n은 1보다 커야함.
    - totalPage = round(m/n)
2. 총페이지 수를 리턴
'''
import math
n = 0

print('게시물의 총 건수를 입력하시오.')
m = input()

print('한페이지의 게시물의 수를 입력하시오.')

while int(n) < 1:
    n = input()
    if int(n) < 1:
        print('다시 입력하시오.')
    else:
        break

totalPage = math.ceil(int(m)/int(n)) #올림함수 math.ceil
print('게시물 총 건수는 %s, 한페이지 게시물 수는 %s, 총페이지 수는 %s입니다.' %(m,n,totalPage))
