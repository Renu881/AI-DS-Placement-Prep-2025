# break and continue

# break example
for num in range(10):
    if num == 5:
        print("Breaking at", num)
        break
    print(num)

# continue example
for num in range(10):
    if num == 2:
        continue  # skips 2
    print(num)
