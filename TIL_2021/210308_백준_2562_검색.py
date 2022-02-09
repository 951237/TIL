nums = []
for i in range(9):
    nums.append(int(input()))
# max 값 구하기
_max = max(nums)

print(_max)
# index 값의 위치를 찾아줌
print(nums.index(_max)+1)