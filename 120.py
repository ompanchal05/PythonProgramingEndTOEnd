#Horizontal bar chart

import matplotlib.pyplot as plt

students =["Om", "Raj","Keya","Swati" , "Ani"]
marks =[85,90,88,70,92]

plt.barh(students, marks)
plt.title("Horizontal Bar Chart")
plt.show()