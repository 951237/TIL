# main.py
# 입력 받기
import itertools
c = int(input())
lst = []
for i in range(c):
    temp = list(map(int, input().split()))
    lst.append(temp)

# 학급만큼 숫자 한줄로 남들기


def make_class_line(n):
    result = ''
    for i in range(n):
        result += str(i+1)
    return result


m = make_class_line(c)


# 모든 경우 구하기
case = list(itertools.permutations((m), c))

# 각 반별 친밀도 구하기


def make_dic(lst):
    result = {}
    for i in range(len(lst)):
        for j in range(len(lst)):
            k = str(i+1)+str(j+1)
            if k[1]+k[0] in result.keys():
                continue
            result[k] = lst[i][j]
    return result


set_score = make_dic(lst)

# 각 케이스별 조합 구하기


def cal_score(c, case):
    lst_t = []
    if case[0] == '1':
        for i in range(c-1):
            temp = str(case[i]) + str(case[i+1])
            lst_t.append(temp)
    return lst_t


# 각 조합에 따른 점수 구하기
lst_sum = []
for j in case:
    sum = 0
    for i in cal_score(c, j):
        if i in set_score.keys():
            sum += set_score[i]
        elif i[1]+i[0] in set_score.keys():
            i = i[1]+i[0]
            sum += set_score[i]
    lst_sum.append(sum)
result = max(lst_sum)
print(result)
