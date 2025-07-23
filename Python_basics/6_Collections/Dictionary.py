# Dictionary: basically a hash tab, it is a collection of {key:value} pairs, ordered and changable.
#   no duplicates are allowed.
#   you can use them to access a specific value by using a key
#   Of course, a key and a value can be anything. For instance, what follows is an example of {Country:Capital}

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# by using the dir function, you can check all of the different attributes and methods related to the dictionary:

# and you can check what each method does via the help method

# to find a value, you can use the get method and pass the key:
print(capitals.get("India"))

# if you try to insert a key that doesn't exist, it'll return "None"
print(capitals.get("Japan"))

# To customize the behavior, you can use an if - else statement:
if capitals.get("Russia"):
    print("The capital exists")
else:
    print("Element not present in the dictionary")
    
# you can update a certain value with the update{key:value} function:
# it updates the value if the key is present, or creates a new pair if not

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

print(capitals)

# to remove an item from the dictionary, you can use the pop(key) method:
capitals.pop("China")
print(capitals)

# if you want to remove the latest inserted pair, you can use the popitem function:
capitals.popitem()
print(capitals)

# and lastly, you can erase the whole dictionary with the clear() function
capitals.clear()
print(capitals)

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# to get all of the keys, without their values, you can use the keys() function, that returns a list object:
keys = capitals.keys()

for key in keys:
    print(key)
    
# to get all of the values in the dictionary, there is the values() methods, that also returns a list object:
values = capitals.values()

for value in values:
    print(value)
    
# to get the pairs, you can use the items() method.
#   this method returns a list of tuples object [(),(),()] that resembles the dictionary (so it's not a dictionary by itself):
items = capitals.items()
for item in items:
    print(item) # each item is a tuple ("Key", "Value")

# to use it more efficiently, you can do as follows:
for key, value in capitals.items():
    print(f"{key}: {value}")