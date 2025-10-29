import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])

# Figure: The canvas
# Ax: Single plot

# the subplot function returns a tuple of two entities:
# a figure object, and a 2D array of axis objects
figure, axes = plt.subplots(2, 2)   # we can therefore decouple the returned tuple

# to fill the single subplots, we access the array:
axes[0, 0].plot(x, x*2, color="red")
# to customize each, we still access the same subplot
axes[0, 0].set_title("x*2")

axes[0, 1].plot(x, x**2, color="green")
axes[0, 1].set_title("x**2")

axes[1, 0].plot(x, x**3, color="blue")
axes[1, 0].set_title("x**3")

axes[1, 1].plot(x, x**4, color="purple")
axes[1, 1].set_title("x**4")
# of course, you can use whatever graph style as you want for each subgraph

plt.tight_layout()  # to avoid overlapsing
plt.show()