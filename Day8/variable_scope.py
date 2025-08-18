# variable_scope.py

x = 10  # Global variable

def local_example():
    x = 5  # Local variable
    print("Local x:", x)

def modify_global():
    global x
    x = 20
    print("Modified global x:", x)

print("Initial global x:", x)
local_example()
print("Global x after local_example:", x)
modify_global()
print("Global x after modify_global:", x)
