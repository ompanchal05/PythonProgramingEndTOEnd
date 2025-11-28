# Simple Line Plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,10,15]

plt.plot(x,y)
plt.scatter(x,y)
plt.title("Simple line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()