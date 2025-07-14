#basically, it is a ternary operator, and that means that this is an inline if-else statement:
# X if condition else Y

num = -5

print("Positive" if num > 0 else "Negative")

# we can also dynamically assign values to variables based on certain conditions
result = "Even" if num%2 == 0 else "Odd"
print(result)

a = 5
b = 4
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num, min_num)