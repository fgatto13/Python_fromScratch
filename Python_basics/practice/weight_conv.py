#Python Weight Converter

units = ["kg", "lbs"]
weight = float(input("insert the weight number: "))
unit = input("enter kg or lbs for unit measure: ")
if unit in units:
    if unit == "kg":
        weight *= 2.205
        unit = "lbs"
    else:
        weight /= 2.205
        unit = "kg"
    print(f"your weight is {round(weight, 2)} {unit}")
else:
    print("invalid unit")