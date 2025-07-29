# 1) Greet user with name
def say_hi(name):
    return f"Hi, {name}!"

print(say_hi("Renuka"))

# 2) Sum of list elements
def sum_list(numbers):
    return sum(numbers)

print("Sum of list:", sum_list([1, 2, 3, 4, 5]))

# 3) Divide numbers with exception handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

print(divide(10, 2))
print(divide(5, 0))

# 4) Recursive sum to n
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

print("Recursive sum of 5:", recursive_sum(5))
