import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Set the style 
style.use("ggplot")

# Text configs
plt.figure("BAR CHART")
plt.suptitle("PLOT TYPES")
plt.title("BAR CHART")
plt.xlabel("X VALUES")
plt.ylabel("Y VALUES")

# Display a grid 
plt.grid(True)

# Set the values
bob = (90, 67, 87, 76)
charles = (80, 80, 47, 66)
daniel = (40, 95, 76, 89)
skills = ("Python", "Java", "Networking", "Machine Learning")
width = 0.2
index = np.arange(4)

# Plot the values, in the correct index and add a label
plt.bar(index, bob, width=width, label="Bob")
plt.bar(index + width, charles, width=width, label="Charles")
plt.bar(index + width * 2, daniel, width=width, label="Daniel")

# Locate the legend
plt.legend(loc="upper left")

# We plot the 4 value for each person
plt.xticks(index + width, skills)
plt.ylim(0, 120)

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")