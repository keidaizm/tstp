class Hexagon:
    def __init__(self,l):
        self.length = l
        
    def calculate_perimeter(self):
        return self.length * 6

hex = Hexagon(10)

print(hex.calculate_perimeter())

