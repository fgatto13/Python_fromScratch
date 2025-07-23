import random

# print(help(random))

# the random library gives us access to different methods to randomly generate values, with flexibility such as range

# to generate a random integer in a given range (i.e. the faces of a dice), we use the randint(a, b) function:
number = random.randint(1, 6)

print(number)

# you can also use variables as range, as long as they,re integers:
low = int(input("insert a: "))
high = int(input("insert b: "))
if low > high:
    temp = low
    low = high
    high = temp
num = random.randint(low, high)
print(num)

# for a random float, you can use the random() method:
num = random.random()
# the output is going to be a floating point number between 0 and 1
print(num)

# you can also pick a random choiche from a sequence, by using the choiche() method:
options = ("rock", "paper", "scissors")
ans = random.choice(options)

print(ans)

# with the shuffle() method, you can shuffle, for instance, a deck of cards:
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

