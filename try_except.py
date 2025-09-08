# try_except.py

# Example 1: Division by zero
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

# Example 2: Invalid input
try:
    value = int("abc")  # invalid conversion
    print("Value:", value)
except ValueError:
    print("Error: Invalid integer conversion!")
