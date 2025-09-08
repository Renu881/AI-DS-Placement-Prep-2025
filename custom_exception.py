# custom_exception.py

class NegativeAgeError(Exception):
    """Custom exception for negative age"""
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
    print("Age is set to:", age)

try:
    set_age(-5)
except NegativeAgeError as e:
    print("Custom Exception:", e)
