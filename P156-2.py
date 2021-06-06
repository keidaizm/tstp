import math

class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius **2 * math.pi

circle = Circle(10)
circlearea = circle.area()

print(circlearea)
print(circle.area())



