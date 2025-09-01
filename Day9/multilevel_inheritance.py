# multilevel_inheritance.py

class Animal:
    def eat(self):
        print("I can eat!")

class Mammal(Animal):
    def walk(self):
        print("I can walk!")

class Dog(Mammal):
    def bark(self):
        print("Woof Woof!")

# Usage
dog = Dog()
dog.eat()
dog.walk()
dog.bark()
