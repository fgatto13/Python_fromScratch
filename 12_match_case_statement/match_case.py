# added in Python 3.10, it is equivalent to switch case
# in C/C++, being a more readable alternative to elif statements

def day_of_week(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        # case _ equals to the default case in C
        case _:
            print("invalid day")
        
day_num = int(input("Insert the number of the day (1 to 7): "))
print(day_of_week(day_num))

# we can also use logical operators such as or, in this case signaled by | :
def is_weekend(day):
    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case "saturday" | "sunday":
            return True
        case _:
            return False

day = input("Insert day of the week: ").lower()
print("Yes" if is_weekend(day) else "No")