import time

# note: default arguments must be defined AFTER positional ones
def count(end, start = 0):
    for x in range (start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")
# now, by defining a default argument, we can assume that it starts from 0:
count(10)
# but we can also make it start at a different starting time:
count(30, 15)