class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
classe Square(Shape):
    def __init__(self, lenght=0):
        Shape.__init__(self)
        self.lenght=lenght

    def area(self):
        return self.length*self.lenghth

x=int(input())
s=Square(x)
print(s.area())
print(Square().area())


