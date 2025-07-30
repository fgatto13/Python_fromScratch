# a JSON file is made of key:value pairs
import json

# we can therefore use a dictionary:
employee = {
    "name": "Eugene",
    "age": 22,
    "job": "Engineer"
}

file_path = "output.json"

try:
    with open(file = file_path, mode = "w") as file:
        # since we're working with json files, the dump method is equivalent to the write method for txt files
        json.dump(employee, file, indent=4) # we can also pass an indent for each key:value pair.
        print(f"the location '{file_path}' was created")
except FileExistsError:
    print(f"the location '{file_path}' already exists")
