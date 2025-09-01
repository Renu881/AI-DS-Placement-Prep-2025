# polymorphism_ducktyping.py

class Laptop:
    def execute(self):
        print("Running a program...")

class Human:
    def execute(self):
        print("Solving a problem...")

def code(obj):
    obj.execute()

# Any object with "execute" method works
l1 = Laptop()
h1 = Human()

code(l1)
code(h1)
