# Compound interest calculator in Python
#
# the formula is as follows:
# 
# A = P*(1 + (r/n))^t
# 
# where:
# - A = final amount
# - P = initial principal balance
# - r = interest rate
# - t = number of time periods elapsed

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle cannot be <= 0")

# we can also use infinite loops by using boolean values:
while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("interest rate cannot be <= 0")
    else:
        break

while time <= 0:
    time = int(input("Enter the number of years: "))
    if time <= 0:
        print("time cannot be <= 0")
        
total = principle * pow((1 + (rate/100)), time)
print(f"Balance after {time} year/s is: ${total:.2f}")