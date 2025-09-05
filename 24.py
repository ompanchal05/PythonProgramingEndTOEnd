#WAP to print the assending and dessening order in using python library and use the adv.python and all by methodes if possible you know about in python

# Importing advanced libraries
import numpy as np
import pandas as pd

# Sample data
data = [45, 12, 89, 33, 76, 23, 5, 90]

print("Original List:", data)

# ------------------ 1. Using Built-in sorted() ------------------
ascending_sorted = sorted(data)  # Ascending by default
descending_sorted = sorted(data, reverse=True)  # Descending
print("\n1. Using sorted():")
print("Ascending:", ascending_sorted)
print("Descending:", descending_sorted)

# ------------------ 2. Using list.sort() ------------------
# Note: sort() modifies the list in place
data_copy = data.copy()
data_copy.sort()  # Ascending
print("\n2. Using list.sort():")
print("Ascending:", data_copy)
data_copy.sort(reverse=True)
print("Descending:", data_copy)

# ------------------ 3. Using NumPy ------------------
np_array = np.array(data)
ascending_numpy = np.sort(np_array)
descending_numpy = np.sort(np_array)[::-1]
print("\n3. Using NumPy:")
print("Ascending:", ascending_numpy)
print("Descending:", descending_numpy)

# ------------------ 4. Using Pandas ------------------
df = pd.DataFrame(data, columns=['Numbers'])
ascending_pandas = df.sort_values(by='Numbers', ascending=True)
descending_pandas = df.sort_values(by='Numbers', ascending=False)
print("\n4. Using Pandas:")
print("Ascending:\n", ascending_pandas['Numbers'].tolist())
print("Descending:\n", descending_pandas['Numbers'].tolist())

# ------------------ 5. Using Python slicing & lambda ------------------
print("\n5. Using lambda with sorted():")
ascending_lambda = sorted(data, key=lambda x: x)  # same as default
descending_lambda = sorted(data, key=lambda x: -x)  # negative for reverse
print("Ascending:", ascending_lambda)
print("Descending:", descending_lambda)