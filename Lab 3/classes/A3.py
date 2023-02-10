from A2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area_of_rectangle(self):
        return self.length*self.width

# a = int(input())
# b = int(input())
# c = Rectangle(a, b)
# print(c.area_of_rectangle())
