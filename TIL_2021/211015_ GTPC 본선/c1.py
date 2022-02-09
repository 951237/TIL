t = int(input())
s = input()


def ship(n, from_pos, to_pos, aux_pos):
    lst_c = []
    if n == 1:
        return 1
    return 1 + ship(n-1, from_pos, aux_pos, to_pos) + ship(n-1, aux_pos, to_pos, from_pos)


print(ship(t, 1, 3, 2))
