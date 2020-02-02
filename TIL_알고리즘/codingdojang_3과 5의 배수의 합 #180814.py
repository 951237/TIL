#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#개요
'''
1. 목표 : 1부터 10까지의 숫자중에서 3과 5의 배수들의 합을 구한다.
'''

#알고리즘
'''
1. 3의 배수를 구한다.
2. 3의 배수들의 합을 구한다.
3. 5의 배수를 구한다.
4. 5의 배수들의 합을 구한다.
5. 3과 5의 배수의 합을 구한다.
'''

#3의 배수를 구한다.
def mutiple(num,endNum):
    list_num = []
    for _a in range(1,endNum+1): #1부터 마지막수까지
        if _a % num == 0: #나머지가 없으면
           list_num.append(_a) # 숫자(배수)를 리스트로 만들기
        else:
            continue
    return sum(list_num) #리스트이 합을 리턴

_3 = mutiple(3,1000) #3의 배수
_5 = mutiple(5,1000) #5의 배수

print(_3+_5)

