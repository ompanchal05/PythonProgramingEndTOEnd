# create a Project of Student Management using class and functions

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Om", [90, 85, 88])
print("Average =", s1.get_avg())
