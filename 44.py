#WAP for the introduction of the  Plotting using PyLab,

# Import PyLab (combines matplotlib and numpy)
from pylab import *

# Create sample data
x = linspace(0, 10, 100)   # 100 points between 0 and 10
y = sin(x)                 # y = sin(x)

# Plot the data
plot(x, y, 'b-', linewidth=2, label='y = sin(x)')   # 'b-' means blue line

# Add labels and title
xlabel('X-axis (radians)')
ylabel('Y-axis (sin values)')
title('Introduction to Plotting using PyLab')

# Add grid and legend
grid(True)
legend()

# Display the plot
show()
