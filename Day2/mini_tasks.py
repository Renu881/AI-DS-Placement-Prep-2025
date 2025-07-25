# Task 1: Make a list of your 3 fav movies. Replace 2nd one, add a 4th, remove 1st.
movies = ["Doctor", "Theri", "Dragon"]
print("Original list:", movies)

# Replace 2nd movie
movies[1] = "VTV"
print("After replacing 2nd:", movies)

# Add a 4th movie
movies.append("Youth")
print("After adding 4th:", movies)

# Remove 1st movie
movies.pop(0)
print("After removing 1st:", movies)


# Task 2: Make a tuple (x, y, z). Print each.
coordinates = (10, 20, 30)
print("x:", coordinates[0])
print("y:", coordinates[1])
print("z:", coordinates[2])


# Task 3: Make a set of subjects you like. Add one, remove one.
subjects = {"Math", "Physics", "Computer Science"}
print("Original subjects:", subjects)

# Add a subject
subjects.add("AI")
print("After adding:", subjects)

# Remove a subject
subjects.remove("Math")
print("After removing:", subjects)


# Task 4: Make a dict for your laptop specs: brand, RAM, SSD. Update RAM.
laptop = {
    "brand": "Dell",
    "RAM": "8GB",
    "SSD": "512GB"
}
print("Original specs:", laptop)

# Update RAM
laptop["RAM"] = "16GB"
print("After updating RAM:", laptop)
