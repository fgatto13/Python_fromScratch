#Python calculator

operators = ["+", "-", "*", "/", "%"]
operator = input("Enter an operator between +, -, *, /, % : ")
if operator in operators:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    elif operator == "/":
        result = num_1 / num_2
    else:
        result = num_1 % num_2
    print(f"result: {round(result, 2)}")
else:
    print("invalid operator")