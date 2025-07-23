#Shopping cart program

item = input("insert the item of your choiche: ")
price = float(input("insert the price: "))
quantity = int(input("insert the number of items: "))
total = price * quantity

print(f"you have bought {quantity} x {item}/s")
print(f"your total is: ${total}")