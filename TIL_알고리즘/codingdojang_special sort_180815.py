#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#개요
'''
- 목표 : n개의 정수를 가진 배열이 있다. 양의 정수와 음의 정수가 섞여 있는데 음의 정수가 앞쪽에 양의 정수가 뒤쪽으로 정렬.
단 순서에는 변함이 없어야 함.
- 문제점
    -
'''

#알고리즘
'''
1. 리스트 2개를 만듦.
    - 플러스, 마이너스
2. n개의 정수를 가진 배열을 반복
    - 0보다 작으면 마이너스 배열에 누적
    - 0보다 크면 플러스 배열에 누적
3. 출력하기
    - 마이너스 리스트 + 플러스 리스트
'''

list_num = ['-1', '1', '3', '-2', '2']

list_plus = []
list_minus = []
for i in range(len(list_num)):
    if int(list_num[i]) > 0:
        list_plus.append(list_num[i]) # 0보다 크면 플러스 리스트에 누적
    else:
        list_minus.append(list_num[i]) #0보다 작으면 마이너스 리스트에 누적

print(list_minus + list_plus) #마이너스 리스트를 먼저 출력하고 이어서 플러스 리스트를 출력
