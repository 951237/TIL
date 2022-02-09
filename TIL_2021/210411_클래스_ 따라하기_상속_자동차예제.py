class Vehicle:
    def __init__(self, make, model, color, price):  # 생성자 메소드
        self.make = make
        self.model = model
        self.color = color
        self.price = price
    
    def set_make(self, make):   # 설정자 메소드
        self.make = make

    def get_make(self):     # 접근자 메소드
        return self.make

    def get_desc(self):
        return f"차량 : {self.make}, {self.model}, {self.color}, {self.price}"

# 클래스의 상속
class Truck(Vehicle):
    def __init__(self, make, model, color, price, payload):     # 생성자 
        super().__init__(make, model, color, price)     # vehicle 상속받기
        self.payload = payload      # 트럭의 인스턴스 변수 생성

    def set_payload(self, payload):     # 설정자
        self.payload = payload

    def get_payload(self):  # 접근자
        return self.payload

def main():
    my_truck = Truck("Tesla", "Model S", "White", 1000, 2000)
    my_truck.set_make("Tesla")
    my_truck.set_payload(2000)
    print(my_truck.get_desc())


# v1 = Vehicle("현대", "아반떼", "흰색", "4천만원")
# v2 = Vehicle("기아", "모닝", "빨강색", "2천만원")
# v1.set_make("기아")
# print(v1.get_desc())
# print(v2.get_desc())

main()