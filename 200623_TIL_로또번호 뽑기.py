import random       # 랜덤함수 호출

def make_num_list():
    num_list = []   # 로또 번호 담을 리스트
    for i in range(1, 46):  # 1부터 45까지
        num_list.append(i)  # 리스트에 담음
    return num_list


# win_set = []    # 랜덤으로 뽑은 로또번호 리스트

# for i in range(0, 5):   # 5세트 숫자 생성
def make_lotte_num():
    num_list = make_num_list()
    win_num_list = []   # 랜덤으로 뽑은 번호 담을 리스트
    for i in range(0, 6):   # 6개의 숫자 뽑기
        r_seed = random.randrange(0, len(num_list))     # 숫자 리스트에서 랜덤으로 숫자 뽑기
        win_num = num_list.pop(r_seed)      # 숫자 리스트에서 뽑은 숫자 없애면서 변수에 저장
        win_num_list.append(win_num)    # 로또번호 리스트에 담기
        win_num_list.sort()     # 리스트 내림차순 정렬
    return win_num_list
# win_set.append(win_num_list)    # 로또번호 리스트에 담기

# for i in win_set:
#     print(i)


# 추출숫자 당첨여부 확인하기

num_lotte = [6, 21, 22, 32, 35, 36]
num_bonus = [16]
print(f'로또당첨번호 : {num_lotte}')


count_cycle = 0
while True:
    win_num_list = make_lotte_num()

    count_cycle += 1

    if (count_cycle % 1000000) == 0:
        print(f'{count_cycle}번째 시도중...')
    else:
        count_lotte = 0
        for i in win_num_list:
            if i in num_lotte:
                count_lotte += 1

        if count_lotte == 6:
            print(f'{count_cycle}차시도')
            print(f'자동추첨 번호 : {win_num_list}')
            print(count_lotte)
            break
        else:
            continue


