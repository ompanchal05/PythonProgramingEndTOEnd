import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'Science', 'English', 'History']
marks = [80, 90, 70, 85]

# Bar Plot
plt.bar(subjects, marks, color='skyblue', edgecolor='Black')

# Customization
plt.title("Bar Plot - Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
