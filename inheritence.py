class Rectangle:
    def __init__(self):
        print("Inside init of Rectangle")
    def area(self,x,y):
        return x*y

class Square(Rectangle):
    def __init__(self):
        print("Inside init of Square")

r = Rectangle()
sq = Square()
area = sq.area(5,5)
print(area)