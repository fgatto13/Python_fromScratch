# Tuple = () ordered and unchangeable, can contain duplicates and it is faster.

# you can only use count and index methods, besides the dir, help, len and in methods:
fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(dir(fruits))
print(len(fruits))
print("pineapple" in fruits)
print(fruits.count("coconut"))
print(fruits[2])

for x in fruits:
    print(x)
    