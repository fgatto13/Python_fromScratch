import matplotlib.pyplot as plt
import numpy as np 

# dictionary with style parameters
line_style = {
    'linewidth': 2,
    'linestyle': '--',
    'marker': 'o',
    'markersize': 8,
    'markerfacecolor': 'red',
    'markeredgewidth': 2,
    'markeredgecolor': 'black',
}

x = np.array([2023, 2024, 2025, 2026, 2027])
y = np.array([15, 30, 25, 60, 50])
z = np.array([5, 15, 10, 20, 25])

# you can customize the plot with various parameters
plt.plot(
    x, 
    y, 
    color='blue',
    **line_style
) # in the docs there are many options for customizing the plot
plt.plot(
    x, 
    z, 
    color='green',
    **line_style
) 
# every plot adds a new line to the same graph, unless you clear it
plt.show()