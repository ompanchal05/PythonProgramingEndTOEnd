import matplotlib.pyplot as plt

# Data: current vs latent values
current = [1, 2, 3, 4, 5, 6, 7]
latent  = [2, 4, 5, 7, 10, 11, 13]

# Scatter plot
plt.scatter(current, latent, color="red", marker="o", s=100)

# Customization
plt.title("Scatter Plot: Current vs Latent", fontsize=14, color="blue")
plt.xlabel("Current Values", fontsize=12, color="green")
plt.ylabel("Latent Values", fontsize=12, color="purple")

# Add grid and labels
plt.grid(True, linestyle="--", alpha=0.6)

# Show
plt.show()

