class Square:
    def __init__(self,x):
        self.side = x

    def area(self):
        return self.side * self.side

sq = Square(4)
sq.side = 6
area = sq.area()
print(area)
