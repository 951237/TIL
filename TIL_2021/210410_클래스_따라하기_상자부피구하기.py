class Box:
    def __init__(self, width = 0, length = 0, height = 0): # 생성자
        self.__width = width
        self.__length = length
        self.__height = height
    
    def setWidth(self, width):  # 값을 변경
        self.__width = width
    
    def setLength(self, length):
        self.__length = length

    def setHeight(self, height):
        self.__height = height

    def getVolume(self):    # 부피구하기
        return self.__width * self.__length * self.__height

    def __str__(self):      # 클래스의 출력형식 지정
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)

box = Box(100, 100, 100)
print(box)
print("상자의 부피는 ", box.getVolume())