#Alias in numpy 

#Maine terko notebook di or bola ki tu use kar na and tu voh notebook use kar rahi hai use alias conseept kehsakte hai


import numpy as np

a = np.array([1,2,3])
b = a

b[0] = 100
print(a)