import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Set the style 
style.use("ggplot")

# Text configs
plt.figure("HISTOGRAM")
plt.suptitle("PLOT TYPES")
plt.title("HISTOGRAM")
plt.text(156, 0.135, "We can add text to a certain location")
plt.xlabel("X VALUES")
plt.ylabel("Y VALUES")

#Change the axis
plt.axis([155, 190, 0, 0.15])

# Display a grid 
plt.grid(True)

# Set X/Y values
x_values = 172 + 4 * np.random.randn(10000)
number_of_values = 100

# Plot the values, norm our the data and add the color
plt.hist(x_values, number_of_values, density=True, facecolor="blue")

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")