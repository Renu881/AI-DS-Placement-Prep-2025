import json

# Writing to a JSON file
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)

# Reading from a JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)


#json.dump() writes Python objects to a file.
#json.load() reads the JSON data from the file
