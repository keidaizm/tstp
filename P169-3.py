class Shape:
    def what_am_i(self):
        print("I am a Shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass


rec = Rectangle()
rec.what_am_i()
        
