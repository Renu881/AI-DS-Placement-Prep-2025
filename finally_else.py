# finally_else.py

try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)
except ValueError:
    print("Please enter a valid integer")
else:
    print("No exceptions occurred!")
finally:
    print("Execution completed (finally block always runs)")
