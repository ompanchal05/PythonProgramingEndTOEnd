#pie chart 

import matplotlib.pyplot as plt

sizes = [40,25,22,15]
labels = ["python", "Java","C++","Others"]

plt.pie(sizes, labels=labels , autopct="%0.1f%%")
plt.title("Programming language popu")
plt.show()