# 1) Even or Odd checker
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2) Sum of first N numbers using for loop
total = 0
for i in range(1, 11):
    total += i
print("Sum of 1 to 10:", total)

# 3) Count down using while loop
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# 4) Multiplication table (nested loop)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("---")

# 5) Print only odd numbers using continue
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print("Odd number:", num)
