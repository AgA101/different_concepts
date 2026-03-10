class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self,other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
class Vector(Point):

    def length(self,other):
        if isinstance(other,Vector):
            return self.dist(other.x,other.y)

    def __str__(self):
        return Vector(self.x,self.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(Point(self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(Point(self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return Vector(Point(self.x * other, self.y * other))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self * other

class Vehile:
    def __init__(self, position):
        if isinstance(position,Point):
            self.position = position
        self.vector = Vector(Point(self.position.x,self.position.y))
        self.Curpos = Point(self.position.x,self.position.y)
        self.is_recording = False
        self._path = []


    def move(self,n):
        self.Curpos += n

class Car(Vehile):
    def __init__(self,position,gas,gas_per_unit):
        self._position = position
        self.__gas = gas
        self.__gas_per_unit = gas_per_unit
    def move(self,n):
        pass
    
a = Point(1,4)

v = Vehile(a)