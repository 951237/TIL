#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#개요
'''
- 목표 : 하루동안(00:00 ~ 23:59)까지의 3이 들어간 시간의 합을 초로 나타내기
'''

#알고리즘
'''
1. 1시까지 3이 들어간 시간의 합 구하기
2. 10시까지 3이 들어간 시간의 합
3. 20시까지 3이 들어간 시간의 합 구하기
4. 
'''

# 1시까지 3이 들어간 시간의 합
list_hour = ['3', '13', '23', '33','43','53']
s = 0
for i in list_hour:
    s = s + int(i)
# print(s * 60)

#1시까지 3이 들어간 시간의 합 반복문
min = 0
for i in range(3, 63, 10):
    min = min + int(i)
# print(min * 60)

#0~2시까지 3이 들어간 시간의 합 반복문
result = 0
for j in range(0,24): #0시부터 23시까지 루프
    # print(j)
    min = 0
    for i in range(3, 63, 10): #3, 13, 23, 33, 43, 53을 반복
        min = min + int(i) #분을 누적 합산
        # j = j + 1
    totalMin = min * 60 #분을 초로 변환
    totalHour = j * 6 * 3600 #시간을 초로 변환
    totalAll = totalMin + totalHour
    print('%s시 부터 %s시 까지의 3이 들어간 시간의 합(초)은 %s초입니다.' %(j, j+1, totalAll))
    result = result + totalAll
print(result)
