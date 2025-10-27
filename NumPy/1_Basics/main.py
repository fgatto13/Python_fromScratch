import numpy as np

# numpy gives us access to arrays, which are faster than standard Python lists
array = np.array([1, 2, 3])
print(array)

# we can use them to perform vectorized operations
# e.g. we can multiply the array with a scalar 
array = array * 2
print(array)

# (doing that with a list would duplicate the content inside the list)
my_list = [1, 2, 3, 4]
print(my_list)
my_list = my_list * 2
print(my_list)