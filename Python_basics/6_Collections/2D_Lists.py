# It is just a list of lists, basically a Matrix

groceries = [["apple", "orange", "banana", "coconut"], 
             ["celery", "carrots", "potatoes"], 
             ["chicken", "fish", "turkey"]]

for list in groceries:
    print(list)
    # or you can use rows and columns indexes to access a specific element:
    print(groceries[0][1])
    # you can also use only one index to select the entire row:
    print(groceries[0])

# another way to display a matrix, you can use nested loop:
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
    
# you can also create a list of Tuples, a Tuple of tuples, or even a set of sets and so on