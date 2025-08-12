n = int(input("Enter a number: "))
flag = True

if n <= 1:
    flag = False
else:
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

print("Prime" if flag else "Not Prime")
