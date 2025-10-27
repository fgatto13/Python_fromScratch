import numpy as np

# multi-dimensional arrays
# zero-dimensional
array_1 = np.array('A')
print(array_1.ndim) # prints the dimension of the array

# one-dimensional
array_2 = np.array(['A', 'B'])
print(array_2.ndim) # prints the dimension of the array

# two-dimensional array (or matrix)
array_3 = np.array([['A', 'B', 'C'],
                    ['D', 'E', 'F'],
                    ['G', 'H', 'I']])
print(array_3.ndim)     # prints the dimension of the array
print(array_3.shape)    # prints the shape of the array (3, 3) 
# when working with multi-dimensional arrays, each entry (list) has to have the same dimension

# with numpy, there is no need to use chain indexing (e.g. [][])
# instead, we can use multidimensional indexing:
print(array_3[0, 1])    # you still need to be within indexing boundaries, otherwise you might get index out of range