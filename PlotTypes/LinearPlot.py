import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Set the style 
style.use("ggplot")

# Text configs
plt.figure("LINEAR PLOT")
plt.suptitle("PLOT TYPES")
plt.title("LINEAR PLOT")
plt.xlabel("X VALUES")
plt.ylabel("Y VALUES")

# Display a grid 
plt.grid(True)

# Set X/Y values
x_values = np.linspace(0, 100, 200)
y_values = np.linspace(0, 100, 200)

# Plot the values, add a color and create a legend
plt.plot(x_values, y_values, "b-", label="Line")

# Locate the legend
plt.legend(loc="upper left")

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")