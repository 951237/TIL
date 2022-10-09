from turtle import *

shape("turtle")
speed(0)

# 나무 프렉탈 그리기 
def tree(size, levels, angle): # 사이즈, 깊이, 각도 설정
	if levels == 0:		# 조건 - 레벨이 '0'이면
		color("green")	# 색깔
		dot(size)	# 점의 크기 설정
		color("black")	# 선의 색깔
		return
	
	forward(size) # 앞으로 
	right(angle) 	# 오른쪽으로 회전 

	tree(size * 0.8, levels -1, angle)	# 크기를 80%, 깊이 -1, 회전 각도는 같게 - 재귀함수

	left(angle *2)		# 왼쪽으로 각도 * 2 전환하기 : 이미 오른쪽으로 회전을 했기때문에 반대편으로 가기 위해서는 2배만큼 돌기

	tree(size * 0.8, levels -1, angle)	# 함수안에서 본인 함수 실행. 선분의 길이를 80%만큼, 깊이를 줄임

	right(angle)	# 오른쪽으로 회전
	backward(size)

# 눈꽃 결정 프렉탈 그리기
def snowflake_side(length, levels):
	if levels ==0:
		forward(length)
		return
	
	length /= 3.0
	snowflake_side(length, levels -1)
	left(60)
	snowflake_side(length, levels - 1)
	right(120)
	snowflake_side(length, levels - 1)
	left(60)
	snowflake_side(length, levels -1)

def create_snowflake(sides, length):
	colors = ["green", "blue", "yellow", "orange"]
	for i in range(sides):
		color(colors[i])
		snowflake_side(length, sides)
		right(360 / sides)

# left(90)
# tree(70, 10, 30)

create_snowflake(4, 200)

mainloop()