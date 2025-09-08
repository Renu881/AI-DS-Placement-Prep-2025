# multiple_exceptions.py

try:
    numbers = [1, 2, 3]
    print(numbers[5])  # IndexError
except ValueError:
    print("Value error occurred")
except IndexError:
    print("Index error occurred")
except Exception as e:
    print("General error:", e)
