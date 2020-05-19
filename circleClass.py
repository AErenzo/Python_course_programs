class Circle:

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def getRadius(self):
        return self.radius

    def getColour(self):
        return self.colour

    def getArea(self):
        area = 3.14195 * self.radius **  2
        return area


c1 = Circle(0.5, 'Blue')
print('Cirle one')
print('Your circles radius is:', c1.getRadius())
print()
print('The colour of your cirle is:', c1.getColour())
print()
print('The area of your circle is:', c1.getArea())

print()

c2 = Circle(0.7, 'Black')
print('Circle 2')
print('Your circles radius is:', c2.getRadius())
print()
print('The colour of your cirle is:', c2.getColour())
print()
print('The area of your circle is:', c2.getArea())


