# format specifiers allow to format a value based on what flags are inserted {value:flags}
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify 
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place a sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
#
# depending on the flag inserted, it'll format the output in a certain way

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1: ${price1:.2f}") #adds a limit to the decimal value: 3.14159 becomes 3.14. f means floating point
print(f"Price 2: ${price2:.2f}")
print(f"Price 3: ${price3:.3f}")

# if you place a number after the column, it will mean the amount of padding used by the string value:
print(f"Price 1: ${price1:10}") 
print(f"Price 2: ${price2:10}")
print(f"Price 3: ${price3:10}")

# if you add a 0 to the front of the number, you fill the padding with zeroes:
print(f"Price 1: ${price1:010}") 
print(f"Price 2: ${price2:010}")
print(f"Price 3: ${price3:010}")

# if you add a < to the front of the number, you left justify the value:
print(f"Price 1: ${price1:<10}") 
print(f"Price 2: ${price2:<10}")
print(f"Price 3: ${price3:<10}")

# if you add a > to the front of the number, you right justify the value (default):
print(f"Price 1: ${price1:>10}") 
print(f"Price 2: ${price2:>10}")
print(f"Price 3: ${price3:>10}")

# if you add a ^ to the front of the number, you center justify the value:
print(f"Price 1: ${price1:^10}") 
print(f"Price 2: ${price2:^10}")
print(f"Price 3: ${price3:^10}")

# if you have positive values, you can add a + after the : to display a plus sign (only with positive values):
print(f"Price 1: ${price1:+}") 
print(f"Price 2: ${price2:+}")
print(f"Price 3: ${price3:+}")

# if add a spacer, you can evenly display the values, even if there are plus and minus signs:
print(f"Price 1: ${price1: }") 
print(f"Price 2: ${price2: }")
print(f"Price 3: ${price3: }")

# by adding a comma, it'll separate the thousands (1,000):
print(f"Price 1: ${price1:,}") 
print(f"Price 2: ${price2:,}")
print(f"Price 3: ${price3:,}")

# you can also mix and match different flags:
print(f"Price 1: ${price1:>+15,.2f}") 
print(f"Price 2: ${price2:>+15,.2f}")
print(f"Price 3: ${price3:>+15,.2f}")