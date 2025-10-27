import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# to slice this array, we'll be using the subscript operator:
# array[start:end:step]
print(array[0:3])       # this prints the first three rows
print(array[1:4])       # this prints the second to fourth row
print(array[0:4:2])     # this prints every two rows
print(array[::2])       # this prints every second row in the whole array
# we can use the slice operator with the multidimensional index:
print(array[:, 0])      # by doing that, we can print the first column
print(array[:, 0:3])    # this will print the first three columns
print(array[:, ::2])    # this prints every second column
print(array[:2, 0:2])   # this results in the first two columns of the first two rows (2x2 matrix)
print(array[2:, 0:2])   # this results in the first two columns of the last two rows