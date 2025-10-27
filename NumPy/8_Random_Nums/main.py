import numpy as np
# let's create a random number generator
rng = np.random.default_rng()       # create a default random number generator    
print(rng.integers(low=1, high=7))  # random integer from 1 to 6, since high is exclusive
# if you need a set of numbers, you can specify the size
print(rng.integers(low=1, high=101, size=10))
# with the size parameter, you can create multi-dimensional arrays
print(rng.integers(low=1, high=101, size=(3,4)))  # 3 rows, 4 columns
# you can also specify a seed manually for reproducibility (gives the same random numbers each time)
rng2 = np.random.default_rng(seed=42)
print(rng2.integers(low=1, high=101, size=10))  # it works like Minecraft seeds!

# for floating point numbers, we use a different method
print(np.random.uniform())  # the uniform method can be used for uniform distribution
# (Each number has an equal chance of being selected) and it returns a float in [0.0, 1.0)
# you can also specify low, high, and size parameters
print(np.random.uniform(low=1.0, high=10.0, size=5))  # 5 random floats between 1.0 and 10.0
# multi-dimensional arrays work here too
print(np.random.uniform(low=1.0, high=10.0, size=(2,3)))  # 2 rows, 3 columns  
# seeds work the same way
np.random.seed(seed=1)  # set the seed for reproducibility for all random functions in numpy.random
print(np.random.uniform(low=-1, high=1, size=(3, 2))) # 3 rows, 2 columns of floats between -1 and 1

# for instance, let's shuffle an array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
np.random.default_rng().shuffle(arr)  # shuffles the array in place
print(arr)

# if you need a random choice from an array, use the choice method
options = np.array(['🍎', '🍌', '🍒', '🥥'])
print(options)
fruit = np.random.default_rng().choice(options)
print(fruit)  # prints a random fruit from the options array
# you can also specify size and replace parameters
fruits = np.random.default_rng().choice(options, size=(3, 3))
print(fruits)  # prints an array of 3 random fruits