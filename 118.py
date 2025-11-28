#Line chart with marker and color

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,10,15]

plt.plot(x, y, marker= 'o' , linestyle = '--')
plt.title("Styled Line Chaart")
plt.grid()
plt.show()