# a for loop executes a block of code for a fixed amount of iterations:

# for instance, by using the range funciton, we can count from 1 to 10 (remember, range ending is exclusive)
import time

print("Iterating from 1 to 10: ")
for x in range(1, 11):
    print(x)
    time.sleep(.5)
print("Done!")
   
for x in reversed(range(1, 11)):
    print(x)
    time.sleep(1)
print("Happy new year!")

# you can iterate over a string as well:

credit_card = "1234-5678-9012-3456"
for i in credit_card:
    print(i)
    time.sleep(.5)
    
# the time.sleep() function allows us to emulate a waiting time,
# so that we can see for each iteration in the loop what is happening
# It pauses the thread for a given amount of time, expressed in seconds
# 
# you can also use continue to skip an iteration, or break to exit the loop in certain conditions:
time_amt = int(input("enter the number of seconds: "))
for x in range (1, 21):
    if x == 20:
        break
    elif x == 13:
        continue
    else:
        print(x)
    time.sleep(time_amt)