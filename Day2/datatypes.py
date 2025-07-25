# Dynamic typing
a = 10
print(a, "is of type", type(a))

a = "Now I'm a string!"
print(a, "is of type", type(a))

# Explicit conversion
x = "123"
num = int(x)
print(num, "is", type(num))

f = "3.14"
f_num = float(f)
print(f_num, "is", type(f_num))

# Type error demo:
# print("5" + 5)  # ❌
# Fix:
print("5" + str(5))  # ✔️
