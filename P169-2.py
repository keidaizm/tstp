class Rectangle:
    def __init__(self,s1,s2,s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3

class Squeare:
    def __init__(self,l1):
        self.l1 = l1

    def calculate_perimeter(self):
        return self.l1 *4

    def change_size(self,c):
        self.l1 += c


    

rec = Rectangle(4,5,6)
print(rec.calculate_perimeter())


squ = Squeare(6)
print(squ.calculate_perimeter())
print(squ.l1)

squ.change_size(6)
print(squ.calculate_perimeter())
print(squ.l1)


        
