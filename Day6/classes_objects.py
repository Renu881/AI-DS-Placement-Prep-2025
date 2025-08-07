class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} scored {self.marks}")

s1 = Student("Renuka", 95)
s1.display()
