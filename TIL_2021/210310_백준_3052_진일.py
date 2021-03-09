nums = []
# 숫자 10개 입력받아서 리스트에 저장하기
for i in range(10):
    nums.append(int(input()))

b = []
for i in nums:
    a = i % 42
    b.append(a)
# 리스트를 딕셔너리로 바꾸면 중복된 값은 모두 삭제 
result = list(dict.fromkeys(b))

# 중복이 삭제된 리스트의 갯수를 세기
print(len(result))