# vectorized math functions
import numpy as np

# vector: single dimension
array = np.array([1.01, 2.5, 3.99])

# numpy has a bunch of built in functions to perform specific operatios
print(np.sqrt(array))   # performs the root square of each elemnent of the array
print(np.round(array))  # rounds all of the elements of the array
print(np.floor(array))  # always rounds down
print(np.ceil(array))   # always rounds up

# there are also built in constants in numpy
print(np.pi)            # greek pi
print(np.e)             # Euler's number

# given an array of radiuses, we'll determine the area of the circle
radii = np.array([1, 2, 3])

print(np.pi * (radii ** 2))

# we can also make element-wise arithmetic
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)          # all of these operations are performed for corresponding elements
print(arr1 - arr2)          # e.g. arr1[0] - arr2[0], arr1[1] - arr2[1] and so on
print(arr1 * arr2)          # it's the same logic that applies to vector's math in discrete mathematics
print(arr1 / arr2)
print(arr1 ** arr2)

# finally, we can use comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100)        # all of them print a boolean FOR EACH element of the array
print(scores >= 60)         # e.g. [True False  True  True  True  True]
print(scores < 60)

# we can also use conditional assignments
scores[scores < 60] = 0     # changes all of the grades lesser than 60 to be 0
print(scores)