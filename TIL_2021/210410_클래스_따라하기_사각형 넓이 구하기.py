class Rectangle:
    def __init__(self, side = 0):   # 생성자
        self.side = side
    
    def get_area(self):     # 넓이구하기
        return self.side * self.side

def print_area(r, n):   # 함수 : 인스턴스와 반복회수 입력
    while n >= 1:
        print(r.side, "\t", r.get_area())
        r.side = r.side + 1
        n = n - 1
    
my_rect = Rectangle()

count = 101
print_area(my_rect, count)
print("사각형의 변 = ", my_rect.side)
print("반복회수 = ", count)