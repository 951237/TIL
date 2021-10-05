# 입력받기
r, c, tr, tc = map(int, input().split())

# 맵의 외곽에 -1을 입력하기 위해서 오른쪽 왼쪽에 각각 1줄씩
# 아래위로 1줄식 더해줘야함. 그래서 입력값에 2씩 더함.
r += 2
c += 2

# 전체 월드 리스트로 입력
_map = [[0] * c for i in range(r)]
# print(_map)

# 갈 수 없는 위치 초기화
for i in range(c):  # 첫줄 -1 입력
    _map[0][i] = -1
    _map[r-1][i] = -1   # 0부터 시작하므로 y값보다 1을 작게 설정

for i in range(r):  # 각 줄의 0, -1 -1 입력
    _map[i][0] = -1
    _map[i][c-1] = -1   # 0부터 시작하므로 x값보다 1을 작게 설정

n = int(input())   # 장애물의 갯수

# 장애물 입력
for i in range(n):
    a, b = map(int, input().split())
    _map[a][b] = -1

# r1의 집의 좌표 : 1 입력
_map[1][1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
    step = 1  # 시작값
    cnt = 0  # 이동값
    for i in range(1, r-1):
        for j in range(1, c-1):
            #             print(i,j)
            if _map[i][j] == step:
                for a in range(4):
                    ni = i + dx[a]
                    nj = j + dy[a]
                    if _map[ni][nj] == 0:
                        _map[ni][nj] = step + 1  # 시작값을 1 → 2 → 3. . . 으로
                        cnt += 1
#                         print(f'좌표위치 : ({i},{j}), 좌표값 : {_map[ni][nj]}, 카운트 : {cnt}')
                        step += 1
    if cnt == 0 or _map[tr][tc]:   # 움직일수 없거나 목표지점에 도착한 경우
        break

if _map[tr][tc] == 0:
    print(-1)
else:
    print(_map[tr][tc] - 1)
