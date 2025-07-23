# Set = {} unordered and immutable, but you can add or remove items. Just like in math, no duplicates allowed
# they're mainly used for storing constants

fruits = {"apple", "orange", "banana", "coconut"}
# you can use many functions from lists, such as dir, help, len and the search method (x in fruits)

# you cannot use the index operator, since a set is unordered
# to add an item, use the add() method:
fruits.add("pineapple")
# to remove an item, use the remove() method:
fruits.remove("apple")
# lastly, you can use the pop function to delete the first element of the set (random, since it is unordered):
fruits.pop()