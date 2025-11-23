import numpy as np

data = np.random.randint(1, 100, (5, 5))
print("DATA:\n", data)

print("\nRow-wise Mean:", np.mean(data, axis=1))
print("Column-wise Mean:", np.mean(data, axis=0))

print("\nValues > 50:", data[data > 50])

print("\nUnique:", np.unique(data))
