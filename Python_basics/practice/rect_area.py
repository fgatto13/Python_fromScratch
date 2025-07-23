#Rectangle area calc: ask the user for width and lenght of the rectangle, typecast it and use the following formula:
# A = w*l 
# to calculate the area and then print it

rect_w = float(input("insert the width: "))
rect_l = float(input("insert the lenght:"))
rect_A = rect_w * rect_l
print(f"the area of the rectangle having width = {rect_w} and lenght = {rect_l} is {rect_A}")