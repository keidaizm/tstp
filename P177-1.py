class Square:
    square_list = []

    def __init__(self,l):
        self.length = l
        self.square_list.append(self.length)

    def print_lentgh(self):
        print("{} by {} by {} by {}.".format(self.length,self.length,self.length,self.length))

   


s1 = Square(2)
s2 = Square(4)
s3 = Square(6)

print(Square.square_list)
