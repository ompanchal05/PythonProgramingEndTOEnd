#4. Basic Plot using Pandas Series and Matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create random data
data = pd.Series(np.random.randn(10))

# Plot graph
data.plot(kind='line', title='Random Data Plot')

plt.xlabel('Index')
plt.ylabel('Random Values')
plt.grid(True)
plt.show()