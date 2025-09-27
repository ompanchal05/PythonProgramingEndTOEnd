"""
Demo: Using NumPy for numerical data + Matplotlib for visualization
---------------------------------------------------------------
We will:
1. Create an array of x-values using NumPy
2. Compute sine and cosine values
3. Perform a small numerical calculation
4. Plot both curves with Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# 1️ Create a range of numbers from 0 to 2π (radians)

x = np.linspace(0, 2 * np.pi, 200)   # 200 equally spaced points

# 2️ Calculate sine and cosine using NumPy's vectorized functions

y_sin = np.sin(x)
y_cos = np.cos(x)

# 3️ Perform some numerical analysis

mean_sin = np.mean(y_sin)            # Average of sine values
max_cos  = np.max(y_cos)             # Maximum of cosine values
print(f"Mean of sin(x): {mean_sin:.4f}")
print(f"Max of cos(x): {max_cos:.4f}")

# 4️ Plot using Matplotlib

plt.figure(figsize=(8, 5))  # Set figure size


# Plot sine

plt.plot(x, y_sin, color='blacl', linewidth=2, label='sin(x)')

# Plot cosine

plt.plot(x, y_cos, color='cyan', linestyle='--', linewidth=2, label='cos(x)')

# Add titles, labels, grid, legend

plt.title("Sine & Cosine Waves", fontsize=16)
plt.xlabel("Angle (radians)", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.axhline(0, color='black', linewidth=0.8)  # x-axis line
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Show the plot

plt.show()
