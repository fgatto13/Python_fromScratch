import matplotlib.pyplot as plt
import numpy as np
# scatter graphs show the relationship between two variables.
# Used to identify a correlation (+, -, None)

# let's create an array of studied hours
x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
# and an array of Grades obtained
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])

# let's create an array of studied hours
x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
# and an array of Grades obtained
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])

# now we need to create the graph
plt.scatter(
    x1, 
    y1,
    color="skyblue",
    alpha=0.5,
    s = 200,
    label="Class A"
)
# and we'll add another set of coordinates
plt.scatter(
    x2,
    y2,
    color="red",
    alpha=0.5,
    s = 200,
    label="Class B"
)

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade") 

# to show the legend
plt.legend()

plt.show()