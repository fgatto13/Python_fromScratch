import matplotlib.pyplot as plt
import numpy as np 
# it is better to use numpy arrays since they're faster and more useful than lists for numerical computations

x = np.array([2023, 2024, 2025, 2026, 2027])
y = np.array([15, 30, 25, 60, 50])

# create the plot
plt.plot(x, y)
# display the plot
plt.show()