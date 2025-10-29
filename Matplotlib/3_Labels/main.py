import matplotlib.pyplot as plt
import numpy as np 

# dictionary with style parameters for the lines
line_style = {
    'linewidth': 2,
    'linestyle': '-',
    'marker': 'o',
    'markersize': 8,
    'markerfacecolor': 'red',
    'markeredgewidth': 2,
    'markeredgecolor': 'black',
}

x = np.array([2023, 2024, 2025, 2026, 2027])
y1 = np.array([15, 30, 25, 60, 50])
y2 = np.array([54, 70, 65, 20, 85])
y3 = np.array([25, 45, 35, 80, 70])

# we'll set a title and labels for the axes
plt.title(
    "Sample Line Plot", 
    fontsize=16, 
    family='aerial', 
    color='purple'
)
plt.xlabel("Year")
plt.ylabel("Values")

plt.plot(
    x, 
    y1, 
    color='blue',
    **line_style
) 
plt.plot(
    x, 
    y2, 
    color='green',
    **line_style
) 
plt.plot(
    x,
    y3,
    color='orange',
    **line_style
)

plt.xticks(x)  # set x-ticks to be the years in x
# to style the ticks, we can use the 'tick_params' method
plt.tick_params(
    axis='both',            # changes apply to both axes
    colors='purple',        # color of the ticks    
)

plt.show()