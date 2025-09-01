# polymorphism_overriding.py

class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()
