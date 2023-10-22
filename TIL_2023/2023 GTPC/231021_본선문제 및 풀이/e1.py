def count_gtpc_combinations(s):
    def backtrack(start, path):
        if len(path) == 4 and path == 'GTPC':
            nonlocal count
            count += 1
            return

        if start >= len(s) or len(path) >= 4:
            return

        for i in range(start, len(s)):
            if s[i] == 'GTPC'[len(path)]:
                backtrack(i + 1, path + s[i])

    count = 0
    backtrack(0, '')

    return count

# 예시 입력
input_string = input()

result = count_gtpc_combinations(input_string.upper())
print(result)
