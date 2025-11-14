import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', color='blue', linestyle='--')
plt.plot(x, y2, label='cos(x)', color='red', linestyle='-.')

plt.xlabel("X")
plt.ylabel("Value")
plt.title("Multiple Graphs on Same Plot")
plt.legend()
plt.grid(True)

plt.show()