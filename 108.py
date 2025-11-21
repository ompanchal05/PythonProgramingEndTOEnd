import matplotlib.pyplot as plt

Data1= [1,2,3,4,5,6,7]
Data2= [2,3,4,5,6,7,8]

plt.scatter(Data1, Data2, marker='o', color='b', label='Data Line')
plt.title('Line Plot with Markers')
plt.xlabel('Data1')
plt.ylabel('Data2')
plt.legend()
plt.grid(True)
plt.show()