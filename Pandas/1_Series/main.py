import pandas as pd
# python library built upon numpy to work with dataframes, basically Excel-like tables

# it uses two main data structures: Series and DataFrame
# Series is a one-dimensional labeled array, similar to a list but with labels (index)
data = [10, 20, 30, 40]
series = pd.Series(data)    # create a Series object from a list
print(series)               # prints the Series with default index (0, 1, 2, 3)
# dtype shows the type of data stored in the Series (in this case, integers 64-bit)
# changing data types will change the metadata
data_floats = [1.5, 2.5, 3.5, 4.5]
series_floats = pd.Series(data_floats)
print(series_floats)        # prints the Series with float data type
# you can also set custom index labels
labels = ['a', 'b', 'c', 'd']
series_custom_index = pd.Series(data, index=labels) # we can pass whatever collection we want as index
print(series_custom_index)  # prints the Series with custom index labels

# if you need to access directly elements, you can use .loc and .iloc (location by lable and integer location)
print(series_custom_index.loc['b'])   # access element with label 'b' (value 20)
print(series_custom_index.iloc[2])    # access element at position 2 (value 30)
# though it is not immune to index out of range errors

# we can also reassign values using loc and iloc
print("Before reassignment:")
print(series_custom_index)
series_custom_index.loc['c'] = 35      # change value at label 'c'
series_custom_index.iloc[0] = 15       # change value at position 0
print(series_custom_index)              # prints the updated Series

# now we'll filter by values
data = [100, 150, 200, 250, 300]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(series[series >= 200])  # prints elements with values greater than or equal to 200

# let's see with a dictionary
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
# to create a series from a dictionary, just pass it to the Series constructor
calorie_series = pd.Series(calories)    # in this case, keys become index labels
print("Calorie Series from Dictionary:")
print(calorie_series)  # prints the Series created from the dictionary
# we can use the same methods as before
print("Accessing value for 'Day 2':")
print(calorie_series.loc["Day 2"])      # access value for "Day 2
# and also change the values
calorie_series.loc["Day 3"] += 500    # increase calories for "Day 3" by 500
print("After updating Day 3 calories:")
print(calorie_series)
# we can do filtering as well
print("Days with calories over 1800:")
print(calorie_series[calorie_series > 1800])  # prints days with calories over 1800
# we can easily store them in a CSV file, since pandas has built-in support for it (.to_csv method)
with open("Pandas/1_Series/calories.csv", "w") as file:
    calorie_series.to_csv(file)  # save the Series to a CSV file