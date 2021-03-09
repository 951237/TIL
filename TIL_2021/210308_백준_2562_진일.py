nums = []
for i in range(9):
    try:
        nums.append(int(input()))
    except:
        print('error')
# 리스트 소팅
sort_nums = sorted(nums)

max = sort_nums[-1]
print(max)
# max값의 위치 찾기 index 함수
print(sort_nums.index(max))

