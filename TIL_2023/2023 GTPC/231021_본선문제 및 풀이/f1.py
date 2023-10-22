def minimum_mutation(binary_string):
    count = 0
    num_zeros = 0

    for bit in reversed(binary_string):
        if bit == '0':
            num_zeros += 1
            if num_zeros >= 2:
                count += 1
                num_zeros = 0
        else:
            if num_zeros > 0:
                count += 1
                num_zeros = 0

    return count

def binary_mutation(binary_string):
    while '0' in binary_string:
        index = binary_string.rfind('0')
        binary_string = binary_string[:index] + '1' + binary_string[index + 1:]
        yield binary_string

    # Check for adjacent 0's and change them to 1's
    while '00' in binary_string:
        index = binary_string.rfind('00')
        binary_string = binary_string[:index] + '11' + binary_string[index + 2:]
        yield binary_string

# 예시 입력
binary_string = str(input())
if '0' not in binary_string:
    print(0)
elif binary_string.count('0') == 1:
    print(1)
else:
    mutations = list(binary_mutation(binary_string))
    lst_result = []

    for i, mutation in enumerate(mutations, start=1):
        result = minimum_mutation(mutation)
        lst_result.append(result)
    print(lst_result[0])
