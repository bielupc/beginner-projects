import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Text configs
plt.figure("SURFACE PLOT")
plt.suptitle("SURFACE PLOT")

# Create the 3D environment 
ax = plt.axes(projection="3d")

# Set X/Y/Z values


def z_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

# Plot the values
ax.plot_surface(X, Y, Z)

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")