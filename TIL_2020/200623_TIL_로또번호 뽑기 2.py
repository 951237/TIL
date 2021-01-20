import random

num_list = []
for i in range(1, 46):
    num_list.append(i)


win_set = []

for i in range(0, 5):
    win_num_list = []
    for i in range(0, 6):
        r_seed = random.randrange(0, len(num_list))
        win_num = num_list.pop(r_seed)
        win_num_list.append(win_num)
        win_num_list.sort()
    win_set.append(win_num_list)

for i in win_set:
    print(i)