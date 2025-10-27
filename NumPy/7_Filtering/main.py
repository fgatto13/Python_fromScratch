import numpy as np

# filtering: selecting elements from an array that match a certain condition
# let's create a 2D array of student ages
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 22],
                 [39, 22, 15, 99, 18, 19, 20, 21]])
# now, let's say we want to filter out the ages of students who are 18 or older
teenagers = ages[ages < 18] # this will create a new array with only the values that satisfy the condition  
print("Teenagers' ages:", teenagers)  # [17 16 15]
# this is called boolean indexing, where we use a boolean condition to index the array
# by assigning it to a new variable, 
# we create a new array with only the filtered values, 
# without modifying the original array

# let's say we want to find the adults
adults = ages[ages >= 18]
print("Adults' ages:", adults)  # [21 19 20 30 18 22 39 22 99 18 19 20 21]
# we can also use multiple conditions using logical operators
# for example, let's find ages between 18 and 25
young_adults = ages[(ages >= 18) & (ages <= 25)]    # we'll use the & operator for "and" similarly to it in C
print("Young adults' ages (18-25):", young_adults)  # [19 20 18 22 22 18 19 20 21]
# similarly, we can use the | operator for "or"
# let's find ages that are between 18 and 65
working_ages = ages[(ages >= 18) & (ages <= 65)]
print("Working ages (18-65):", working_ages) 
# we can filter the even values
even_ages = ages[ages % 2 == 0]
print("Even ages:", even_ages)
# or we can do odds
odd_ages = ages[ages % 2 != 0]
print("Odd ages:", odd_ages)
# if you need to preserve the original shape of the array, you can use the np.where() function
# let's create a new array where we set ages above or equal to 18 to 0
modified_ages = np.where(ages >= 18, ages, 0)
print("Modified ages (ages >= 18 set to 0):", modified_ages)
# in this case, np.where() takes three arguments:
# 1. the condition (ages >= 18)
# 2. the value to set where the condition is True (ages)
# 3. the value to set where the condition is False (0)
# this way, we preserve the original shape of the array while modifying its values based on the condition