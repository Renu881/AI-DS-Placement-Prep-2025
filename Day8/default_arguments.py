# default_arguments.py

def greet(name="Guest"):
    print(f"Hello, {name}!")

def power(base, exponent=2):
    return base ** exponent

# Calls
greet()
greet("Renuka")
print("Square of 5:", power(5))
print("Cube of 3:", power(3, 3))
