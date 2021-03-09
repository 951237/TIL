lst_input = []
for i in range(3):
    lst_input.append(int(input()))

result = lst_input[0] * lst_input[1] * lst_input[2]
list_result = list(str(result))

for i in range(10):
    # lst.count(i) 리스트내의 i의 갯수를 카운트 
    print(list_result.count(f'{i}'))

