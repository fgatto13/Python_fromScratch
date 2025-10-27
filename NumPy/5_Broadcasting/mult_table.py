import numpy as np

# let's create a multiplication table using broadcasting
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])            # only one row
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])   # only one column for each row
print(array1.shape)   # (1, 10)
print(array2.shape)   # (10, 1)
# we can broadcast them together, resulting in a (10, 10) multiplication table
multiplication_table = array1 * array2
print(multiplication_table)