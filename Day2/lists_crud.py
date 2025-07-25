# Create
fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

# Read
print("First fruit:", fruits[0])

# Update
fruits[1] = "mango"
print("After update:", fruits)

# Insert at position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# Remove by value
fruits.remove("cherry")
print("After remove:", fruits)

# Pop last item
last = fruits.pop()
print("Popped:", last)
print("After pop:", fruits)

# Length
print("How many fruits?", len(fruits))

# Loop through
for f in fruits:
    print("Fruit:", f)
