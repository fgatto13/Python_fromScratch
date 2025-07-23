# a list comprehension is a concise way to create lists in Python
#   they're more compact and easier to read than traditional loops
#   a list comprehension follows the following formula:
#   list_name = [expression for value in iterable if condition]
#   if is optional, expression is the operation to perform in each iteration

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
square = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(square)

# we can use them for strings, too:
fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits]

print(fruits)

