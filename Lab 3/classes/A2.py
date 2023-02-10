class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area_of_square(self):
        return self.length**2
# a = int(input())
# b = Square(a)
# print(b.area_of_square())
