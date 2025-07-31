import csv

# Writing to a CSV file
data = [["Name", "Age", "Country"],
        ["Alice", 30, "USA"],
        ["Bob", 25, "UK"],
        ["Charlie", 35, "Canada"]]

with open("people.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open("people.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#csv.writer is used for writing data to CSV files.
#csv.reader is used for reading data from CSV files.
