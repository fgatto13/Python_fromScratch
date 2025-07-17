# an iterable is an object or a collection that can return its elements one at a time
#   you can therefore iterate the element in a loop

# a list is iterable
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
    
for num in reversed(nums):
    print(num)

# same goes for tuples:
nums_2 = (1, 2, 3, 4, 5)
for num in nums_2:
    print(num)
    
for num in reversed(nums_2):
    print(num)
    
# and finally for sets too, but they're not reversible:
nums_3 = {1, 2, 3, 4, 5}
for num in nums_2:
    print(num)
    
# a string is also iterable, since it is an array of characters:
name = "Francesco"
for char in name:
    print(char, end=" ")
    
# lastly, when it comes to dictionaries, you can iterate over them, 
# but remember that being a list of {key:value} pairs you need to specify what you want to access:
my_dict = {"A": 1, "B": 2, "C": 3, "D": 4}

for key in my_dict.keys():
    print(key)
    
for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")
    
# of course, the same applies to 2d lists and multidimensional arrays, 
# you just need to use nested loops based on your necessities