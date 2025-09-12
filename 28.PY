import matplotlib.pyplot as plt

# Data
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]

# Histogram
plt.hist(data, bins=5, color='purple', edgecolor='black')

# Customization
plt.title("Histogram - Frequency Distribution")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.show()
