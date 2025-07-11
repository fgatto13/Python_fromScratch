#given a rectangular triangle, by using Pithagora's theorem, we can determine its hypotenuse: sqrt(c^2 + C^2)
import math

a = float(input("insert the first side: "))
b = float(input("insert the second side:"))

hypo = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"by using Pithagora's theorem, given a rectangular triangle having side a:{a}, and side b:{b}, the hypotenuse is = {round(hypo, 2)}")