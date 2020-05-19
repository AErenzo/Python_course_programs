import math

class Point:
    __xCord = 0
    __yCord = 0

    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        self.__xCord = x

    def setY(self, y):
        self.__yCord = y

    def getY(self):
        return __yCord
    
    def getX(self):
        return __xCord

class Circle(Point):
    __radius = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius

    def calcArea(self):
        return math.pi * self.__radius ** 2



P = Point(10, 20)

C = Circle(10, 20, 3.7)

print(C.calcArea())
print()
print('Point members:', P.__dict__)
print('Circle members:', C.__dict__)

        
