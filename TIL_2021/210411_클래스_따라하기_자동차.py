class Car:
    def __init__(self, speed = 0, gear = 1, color = "white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color

    def set_speed(self, speed):
        self.__speed = speed

    def set_gear(self, gear):
        self.__gear = gear
    
    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return '( %d, %d, %s)' %(self.__speed, self.__gear, self.__color)


my_car = Car()
my_car.set_gear(3)      # 기어 3으로 설정
my_car.set_color("White")   # 차 색깔을 white로 설정
my_car.set_speed(100)   # 차의 스피드 수정
print(my_car)