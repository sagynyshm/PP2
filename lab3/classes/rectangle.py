class Shape():    def __init__(self):
        pass    def area(self):
        return 0
class Rectangle(Shape):    def __init__(self, length=0, width=0):
        Shape.__init__(self)        self.length=length
        self.width=width    def area(self):
        return self.length*self.width
a=int(input())b=int(input())
r=Rectangle(a,b)print(r.area())
