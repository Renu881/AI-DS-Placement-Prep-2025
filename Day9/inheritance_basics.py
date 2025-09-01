# inheritance_basics.py

# Parent Class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_details(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")

# Child Class
class Car(Vehicle):
    def __init__(self, brand, wheels, fuel_type):
        # call parent constructor
        super().__init__(brand, wheels)
        self.fuel_type = fuel_type

    def show_details(self):
        # overriding parent method
        print(f"Brand: {self.brand}, Wheels: {self.wheels}, Fuel: {self.fuel_type}")

# Usage
v1 = Vehicle("Generic", 2)
v1.show_details()

c1 = Car("Tesla", 4, "Electric")
c1.show_details()
