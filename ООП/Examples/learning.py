from random import *
class Pupil:
    def __init__(self):
        self.k = []
    def take(self,i):
        self.k.append(i)
    def mis(self):
        h = randint(0,2)
        h1 = self.k[h]
        self.k[h] = ''
        return h1
    def theft(self, f):
        self.f = f
    def out2(self):
        return '%s'%self.f
    
class information:
    def __init__(self, info):
        self.info = info
    def extract(self, i):
        self.cur = self.info[i]
        return '%s'%self.cur

class Teacher:
    def into(self, p):
        self.p = p
    def out(self):
        return '%s'%self.p

inform = information(['red = красный','blue = синий','green =  зеленый','yellow = желтый'])
t = Teacher()
p1 = Pupil()
p2 = Pupil()
t.into(inform.extract(2))
p1.take(t.out())
print('1-ый ученик пока еще знает только', *p1.k)
t.into(inform.extract(0))
p1.take(t.out())
p2.take(t.out())
t.into(inform.extract(1))
p1.take(t.out())
p2.take(t.out())
print('1-ый знает', *p1.k)
print('2-ый знает', *p2.k)
print('1-ый ученик зыбыл  перевод',p1.mis())
print('1-ый знает',*p1.k)
p2.theft(inform.extract(3))
p2.take(p2.out2())
print('2-ый узнал', *p2.k)
