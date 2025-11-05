#WAP for the numpy all opration and all posiible string and integer and all end to end cover the numpy 

import numpy as np

print("Numpy a Version:" , np.__version__)

arr_int = np.array([1,2,3,4,5])
arr_float = np.array([1.2,2.3,5.2,2.2,5.5])
arr_str = np.array(["om","AI","Data","Science"])

print ("\nInterger Array:" , arr_int)
print ("Float Array:" , arr_float)
print ("Interger Array:" , arr_str)

print ("\n Array shape:" , arr_int.shape)
print("Array Data type:" , arr_float.dtype)

arr = np.array([10, 20, 30, 40, 50])
print("\nOriginal Array:", arr)
print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Slice (1:4):", arr[1:4])