class Duck:
    def sound(self):
        print("Qarck")

class Dog:
    def sound(self):
        print("Bark")


for animal in Duck(), Dog():
    animal.sound()