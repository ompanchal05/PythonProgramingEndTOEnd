#Bar Chart 

import matplotlib.pyplot as plt

students =["Om", "Raj","Keya","Swati" , "Ani"]
marks =[85,90,88,70,92]

plt.bar(students,marks)
plt.title("student marks bar charts")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()