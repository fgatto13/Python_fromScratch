import numpy as np
# aggregate functions: summarize data and usually return a single value

# let's create a 2D array
array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])
# to sum all the values in the array, we can use the sum() function
total_sum = np.sum(array)
print("Total sum:", total_sum)  # 55
# we can also compute the mean (average) of all values using the mean() function
mean_value = np.mean(array)
print("Mean value:", mean_value)  # 5.5
# we can also find the standard deviation using the std() function (measure of spread of the data)
std_deviation = np.std(array)
print("Standard Deviation:", std_deviation)  # ~2.872581
# for variance, we can use the var() function
variance_value = np.var(array)
print("Variance:", variance_value)  # 8.25
# we can also find the minimum and maximum values using min() and max() functions
min_value = np.min(array)
max_value = np.max(array)
print("Minimum value:", min_value)  # 1
print("Maximum value:", max_value)  # 10
# we can also determine the index of the minimum and maximum values using argmin() and argmax() functions
min_index = np.argmin(array)
max_index = np.argmax(array)
print("Index of Minimum value:", min_index)  # 0
print("Index of Maximum value:", max_index)  # 9

# with your set of data, you can select an access, e.g., rows or columns, to perform the aggregation on
print(np.sum(array, axis=0))  # sum for each column
print(np.sum(array, axis=1))  # sum for each row

# other useful aggregate functions include:
# np.median(): computes the median value
median_value = np.median(array)
print("Median value:", median_value)  # 5.5
# np.percentile(): computes the nth percentile of the data
percentile_25 = np.percentile(array, 25)
print("25th Percentile:", percentile_25)  # 4.25
# np.any(): checks if any element in the array is True (non-zero)
any_nonzero = np.any(array > 0)
print("Any non-zero elements:", any_nonzero)  # True
# np.all(): checks if all elements in the array are True (non-zero)
all_nonzero = np.all(array > 0)
print("All non-zero elements:", all_nonzero)  # False
# these functions are very useful for data analysis and summarization tasks
