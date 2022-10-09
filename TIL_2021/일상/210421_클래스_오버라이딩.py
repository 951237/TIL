class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "알 수 없음."

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class cat(Animal):
    def speak(self):
        return "야옹!"

animal_list = [Dog("dog1"), Dog("dog2"), cat('cat1')]

for a in animal_list:
    print(a.name + ":" + a.speak())
    