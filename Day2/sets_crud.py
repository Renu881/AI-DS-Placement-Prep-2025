# Create set (duplicates auto-removed)
nums = {1, 2, 2, 3, 4}
print("Set:", nums)

# Add
nums.add(5)
print("After add:", nums)

# Remove
nums.remove(2)
print("After remove:", nums)

# Union
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)

# Intersection
print("Intersection:", a & b)

# Difference
print("A minus B:", a - b)
