tup = ((1, 2, 3), 
       (4, 5, 6), 
       (7, 8, 9), 
       ("*", 0, "#"))

for row in tup:
    for x in row:
        print(x, end=" ")
    print()