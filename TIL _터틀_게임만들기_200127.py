import turtle

wn = turtle.Screen()
wn.title('Making Game')
wn.bgcolor('green')
wn.setup(width = 800, height = 600)

# 게이머 추가
player1 = turtle.Turtle()
player1.speed(0)
player1.penup()
player1.shape("square")
player1.color('white')
player1.goto(0, -250)


wn.mainloop()
