import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Set the style 
style.use("ggplot")

# Text configs
plt.figure("SCATTER PLOT")
plt.suptitle("PLOT TYPES")
plt.title("SCATTER PLOT")
plt.xlabel("X VALUES")
plt.ylabel("Y VALUES")

# Display a grid 
plt.grid(True)

# Set X/Y values
x_values = np.random.rand(50)
y_values = np.random.rand(50)

# Plot the values
plt.scatter(x_values, y_values)

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")