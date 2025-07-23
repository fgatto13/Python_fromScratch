# the time.sleep() function allows us to emulate a waiting time,
# so that we can see for each iteration in the loop what is happening
# It pauses the thread for a given amount of time, expressed in seconds
import time

print("Countdown timer⏲️: ")
time_amt = int(input("enter the number of seconds: "))
for x in range (time_amt, 0, -1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!⏰")