class Car:
    def __init__(self, speed):
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def get_desc(self):
        return "출력 = (" + str(self.speed) + ")"

class SportCar(Car):        # 상속할 때는 부모 클래스를 넣어주기
    def __init__(self, speed, turbo):
        super().__init__(speed)     # 상속시  super(). 로 init 하기
        self.turbo = turbo

    def set_turbo(self, turbo):
        self.turbo = turbo

obj = SportCar(100, True)
print(obj.get_desc())
obj.set_turbo(False)