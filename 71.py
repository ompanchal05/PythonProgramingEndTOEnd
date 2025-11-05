# ===============================================
# NumPy Slicing Example (Step-by-Step Explanation)
# Author: Om Panchal
# ===============================================

import numpy as np

# Create 2D NumPy array
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original Array (data):\n", data)
print("-" * 50)

# ------------------------------------------------
# 1️⃣ data[0:2, 0:2]
print("1️⃣ data[0:2, 0:2]  → First 2 rows and first 2 columns")
result1 = data[0:2, 0:2]
print(result1)
print("→ Selects rows [0,1] and columns [0,1] (Top-left 2x2 block)")
print("-" * 50)

# ------------------------------------------------
# 2️⃣ data[::-1]
print("2️⃣ data[::-1]  → Reverse the order of rows (flip vertically)")
result2 = data[::-1]
print(result2)
print("→ Rows reversed, columns unchanged")
print("-" * 50)

# ------------------------------------------------
# 3️⃣ data[:, ::-1]
print("3️⃣ data[:, ::-1]  → Reverse columns (flip horizontally)")
result3 = data[:, ::-1]
print(result3)
print("→ Each row is reversed, rows stay same")
print("-" * 50)

# ------------------------------------------------
# 4️⃣ data[::-1, ::-1]
print("4️⃣ data[::-1, ::-1]  → Reverse both rows and columns (flip both ways)")
result4 = data[::-1, ::-1]
print(result4)
print("→ Rotates the entire array by 180°")
print("-" * 50)

# ------------------------------------------------
# 5️⃣ data[1:2, 1:2]
print("5️⃣ data[1:2, 1:2]  → Select row index 1 and column index 1")
result5 = data[1:2, 1:2]
print(result5)
print("→ Single element [5], but in 2D format (shape (1,1))")
print("-" * 50)

# ------------------------------------------------
# ✅ Summary of all results
print("\n✅ Summary of Slicing Operations:")
print("data[0:2, 0:2] =>\n", result1)
print("data[::-1] =>\n", result2)
print("data[:, ::-1] =>\n", result3)
print("data[::-1, ::-1] =>\n", result4)
print("data[1:2, 1:2] =>\n", result5)
