# multiple_inheritance.py

class Engine:
    def engine_type(self):
        return "V8 Engine"

class Wheels:
    def wheel_count(self):
        return 4

# Child class inherits from multiple parents
class SportsCar(Engine, Wheels):
    def show_specs(self):
        print(f"Specs: {self.engine_type()} with {self.wheel_count()} wheels.")

car = SportsCar()
car.show_specs()
