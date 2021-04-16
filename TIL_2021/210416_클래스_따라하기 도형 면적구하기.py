class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        print("계산 할 수 없음.")

    def perimeter(self):
        print("계산할 수 있음.")

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

r = Rectangle(0, 0, 100, 200)
print("사각형의 면적은 : ", r.area())
print("사각형의 둘레 : ", r.perimeter())
