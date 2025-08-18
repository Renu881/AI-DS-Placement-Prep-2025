# lambda_functions.py

# Lambda for addition
add = lambda a, b: a + b
print("Sum:", add(3, 5))

# Lambda for square
square = lambda x: x * x
print("Square:", square(6))

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares list:", squares)
