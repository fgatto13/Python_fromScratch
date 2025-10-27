# broadcasting: performing operations on arrays of different shapes
# It works by "stretching" the smaller array across the larger one so that they have compatible shapes
import numpy as np

# we can have two situations:
# 1. dimensions have the same size
# 2. one of the dimensions is of size 1

# let's create two arrays
array1 = np.array([[1, 2, 3, 4]])      
array2 = np.array([[1],[2],[3],[4]])

print("Array 1 shape:", array1.shape)   # (1, 4)
print("Array 2 shape:", array2.shape)   # (4, 1)

# since one of the dimensions is of size 1, we can broadcast these arrays together
print(array1 * array2)

# basically, broadcasting acts as matrix multiplication in this case
# in fact, we're in the case of a matrix m, q and a matrix q, n, 
# resulting in a matrix m, n (in that case 4, 4)
# 
# for that reason, we cannot broadcast two arrays if both dimensions are different from 1 
# and different from each other

# let's see another example
array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9,10,11,12],
                   [13,14,15,16]])      
array2 = np.array([[1],[2],[3],[4]])
# now, we have array1 of shape (4, 4) and array2 of shape (4, 1)
# so, we're in the case of two matching dimensions, therefore we can broadcast them
print(array1 * array2)
# we're basically performing a multiplication between a vector (being array2) and each row of the matrix (array1)

# let's see what happens if we increment the number of columns of array2
array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9,10,11,12],
                   [13,14,15,16]])      
array2 = np.array([[1, 2],[2, 3],[3, 4],[4, 5]])
print(array1 * array2)
# in that case, that won't work, since broadcasting applies to the number of columns, 
# and not only they don't match,
# but neither of them is equal to 1