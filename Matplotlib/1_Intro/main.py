# matplotlib is a library for creating static, animated, and interactive visualizations in Python.
import matplotlib.pyplot as plt
# pyplot is a collection of functions that make matplotlib work like MATLAB.

# to crete a simple line plot, we'll need some x and y coordinates
x = [2023, 2024, 2025, 2026, 2027]
y = [15, 30, 25, 60, 50]

# to crete the plot, we use the plot() function from pyplot
plt.plot(x, y)
# to display the plot, we use the show() function from pyplot
plt.show()

# the defaul behavior for plot is to start at 0 and increment by .5 for each point, if no x values are provided
