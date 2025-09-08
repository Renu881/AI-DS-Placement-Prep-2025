# mini_tasks.py

# Task 1: Handle invalid input
try:
    marks = int(input("Enter your marks: "))
    print("Marks:", marks)
except ValueError:
    print("Error: Enter numbers only!")

# Task 2: Safe division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter integers only")

# Task 3: File handling with exception
try:
    with open("non_existing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found")
