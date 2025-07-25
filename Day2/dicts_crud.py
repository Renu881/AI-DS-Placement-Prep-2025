student = {"name": "Renuka", "age": 21}

# Read
print("Name:", student["name"])

# Safe read
print("Branch:", student.get("branch", "Not set"))

# Add
student["branch"] = "AI & DS"
print("Added branch:", student)

# Update
student["age"] = 22
print("Updated age:", student)

# Delete
del student["age"]
print("After delete:", student)

# Keys, Values, Items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Loop
for key, value in student.items():
    print(f"{key} -> {value}")
