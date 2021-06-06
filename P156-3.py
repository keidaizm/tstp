class Triangle:
    def __init__(self,h,l):
        self.height = h
        self.length = l
        
    def area(self):
        return self.height * self.length /2

tri = Triangle(10,20)

print(tri.area())

