#numpy array 

import numpy as np

arr1 = np.array ([1,2,3,4])
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Using built-in functions
zeros_arr = np.zeros((2, 3))    # 2x3 array of zeros
ones_arr = np.ones((3, 3))      # 3x3 array of ones
range_arr = np.arange(0, 10, 2) # Array from 0 to 8 with step 2
lin_arr = np.linspace(0, 1, 5)