class Person:
    count_a = 2

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'Person<name={self.name}>'

    def __eq__(self, other):
        return self.name == other.name


    def greet(self):
        print(f'Hi {self.name}!')

me = Person('ni')
you = Person('li')
print(me,you)

me.greet()
you.greet()

Person.count_a = 5

clone = Person('ni')
print(me == clone)


