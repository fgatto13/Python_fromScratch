import random

# print(help(random))

# the random library gives us access to different methods to randomly generate values, with flexibility such as range

# to generate a random integer in a given range (i.e. the faces of a dice), we use the randint(a, b) function:
number = random.randint(1, 6)

print(number)

# you can also use variables as range, as long as they,re integers:
low = int(input("insert a: "))
high = int(input("insert b: "))
num = random.randint(low, high)
print(num)