# collection = a "container" of values, so it is a variable that contains multiple variable values:
# List = [] ordered and changeable. It can contain duplicates

# starting with lists, these are similar to arrays, and the synthax is as follows:
fruits = ["apple", "orange", "banana", "coconut"]
# we can use indexing to access a specific position. If the position doesn't contain a value, you get an index error
print(fruits[0])

for x in fruits:
    print(x)

# functions:
print(dir(fruits)) # shows all of the methods linked to lists

# you can check how many components are inside a list with len operator:
print(len(fruits))

# you can also check if a specific element is inside the list or not:
print("apple" in fruits) # returns a boolean value 0

# you can also append an element (meaning it adds an element at the end of the list):
fruits.append("pineapple")

# you can remove a specific item from the list:
fruits.remove("apple")

# you can insert an item in a specific position:
fruits.insert(2, "watermelon")

# you can sort, in this case in alphabetical order:
fruits.sort()

# you can reverse the order of the items in the list:
fruits.reverse()

# you can clear a list (meaning you can erase all of its elements):
fruits.clear()

# you can search for the index of a specific item:
fruits.index("banana")

# since it is a list, you can count the number of instances of a specific item:
fruits.count("apple")