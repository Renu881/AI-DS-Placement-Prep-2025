# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Day 5 file handling!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#Explanation:

#open() is used to open a file.

#"w" mode is for writing to the file. "r" mode is for reading from it.

#with open() ensures that the file is automatically closed after use.
