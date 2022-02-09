#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#개요
'''
1. 목표 : 탭을 공백 4개로 바꾼다.
2. 문제점 : 소스는 탭과 공백이 섞여 있다.
'''

#알고리즘
'''
1. 코드를 리스트로 만든다.
2. 리스트를 하나씩 검사한다.
3. 탭일경우 공백4개로 바꾼다.

'''
txt_code = 'aaaaa                   bbbacdadc'

def tabToSpace(txt):
    return txt.replace('\t'," ")

_a = tabToSpace(txt_code)

#todo 탭이 빈칸으로 바뀌지 않음. 다시 확인.
print(_a)
