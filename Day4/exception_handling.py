try:
    num = int(input("Enter a number: "))
    print("100 divided by your number is:", 100 / num)
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("This always runs.")
