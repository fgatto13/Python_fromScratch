#knowing that the circumference of a circle is C = 2 * pi * r, r being the radius of the circle
#take the radius as an input from the user and use it to calculate the circumference of the circle
import math

radius = float(input("insert radius: "))
circ = 2 * math.pi * radius

print(f"the circumference of a circle having radius = {radius} is {round(circ, 2)}cm")

#by using the formula to calculate the area: A = pi * radius^2, we can determine its value using the pow() function
area = math.pi * pow(radius, 2)

print(f"the area of a circle having radius = {radius} is {round(area, 2)}cm^2")