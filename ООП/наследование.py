class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person<name={self.name}, age={self.age}'

class Developer(Person):
    def __init__(self, name,age, skills):
        super().__init__(name,age)
        self.skills =skills

    def __str__(self):
        return f'Person<name={self.name}, age={self.age}, skills={self.skills}'

class Student(Person):
    pass

developer = Developer("Vasa", 27, ['Python','Java'])
student = Student("Petya", 23)
print(developer)
print(student)