_len_nums = input()
# 입력을 받아서 띄어쓰기로 나눈후 숫자로 바꿔서 리스트로 저장
lst_num = list(map(int, input().split()))
# 리스트의 최대값 구하기
_max = max(lst_num)

# 최대값을 구해서 리스트에 저장하기
a = []
for i in lst_num:
    temp = i/_max * 100
    a.append(temp)

# 리스트의 평균구하기 
_avg = sum(a,0.0) / len(a)
print(_avg)