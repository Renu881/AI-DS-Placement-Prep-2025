# raise_custom.py

def withdraw(amount):
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative")
    print(f"Withdrawing {amount}...")

try:
    withdraw(-100)
except ValueError as e:
    print("Error:", e)
