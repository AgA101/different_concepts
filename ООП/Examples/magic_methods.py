class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self,other):
        if isinstance(other, Point):
            return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

class Vector(Point):
    def length(self):
        return self.distance(Point(0,0))

    def __str__(self):
        return Vector(self.x,self.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.x - other.x, self.y - other.y

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return self.x * other, self.y * other
        elif isinstance(other, Vector):
            return self.x * other + self.y * other

    def __rmul__(self, other):
        return self * other


a = Point(0, 0)
b = Point(3, 0)
v1 = Vector(3,3)
v2 = Vector(-7,5)

print(v1.length())
print(v1 - v2)
print(v1 * 2)
print(3 * v2)
print(v1 * v2)