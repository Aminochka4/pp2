class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, self2):
        D = ((self.x - self2.x)**2 + (self.y - self2.y)**2)**0.5
        return D 

# p1 = Point(50, 100)
# p2 = Point(30, 70)
# print(p1.dist(p2))
# p1.move(70, 25)
# p1.show()

