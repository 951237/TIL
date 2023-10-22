def diffy_game_count(a, b, c, d):
    count = 0
    while a != 0 or b != 0 or c != 0 or d != 0:
        # Calculate the new values for a, b, c, and d
        new_a = abs(b - a)
        new_b = abs(c - b)
        new_c = abs(d - c)
        new_d = abs(a - d)

        # Update the values of a, b, c, and d
        a, b, c, d = new_a, new_b, new_c, new_d

        # Increment the count
        count += 1

    return count

a, b, c, d = map(int, input().split())  # 행렬의 크기 입력 받기

result = diffy_game_count(a, b, c, d)
print(result)
