#in this section, you're gonna find logical operators: and, or, not:
# and: both conditions have to be true for the statement to be true
# or: at least one condition has to be true for the statement to be true
# not: if the condition is true, then the statement is false and viceversa

#let's start by the or:
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")

#to use the and operator, both conditions must be true in order to execute the true condition:
temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It's HOT! 🥵")
else:
    print("it's quite chilly outside 😶‍🌫️")
    
#to use the not, we want to check if something is NOT true or is NOT false
#basically, the not operator inverts the bool condition, so if it is true, then not makes it false and viceversa
temp = 30
is_sunny = True

if not is_sunny:
    print("It's HOT! 🥵")
else:
    print("it's quite chilly outside 😶‍🌫️")