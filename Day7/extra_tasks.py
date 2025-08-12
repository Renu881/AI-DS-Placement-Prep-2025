# Task 1: Reverse a string
def reverse_string(s):
    return s[::-1]

# Task 2: Count Vowels
def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

# Task 3: Find Factorial (Iterative)
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Task 4: Find Max/Min in List
def find_max_min(lst):
    return max(lst), min(lst)

# Testing each task
print(reverse_string("Hello"))
print(count_vowels("Hello World"))
print(factorial(5))
print(find_max_min([1, 2, 3, 4, 5]))
