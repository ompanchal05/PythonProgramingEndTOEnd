# -------------------------------
# ONE SINGLE PYTHON FILE
# Day 1 to Day 12 – All-in-One
# -------------------------------

print("\n--- FUNCTIONS ---")

def add(a, b):
    return a + b

def square(x):
    return x * x

print("Add:", add(10, 20))
print("Square:", square(5))


# -------------------------------
print("\n--- LAMBDA ---")

cube = lambda n: n*n*n
print("Cube (lambda):", cube(3))


# -------------------------------
print("\n--- LIST COMPREHENSION ---")

nums = [i for i in range(1, 6)]
even_nums = [i for i in nums if i % 2 == 0]

print("Numbers:", nums)
print("Even Numbers:", even_nums)


# -------------------------------
print("\n--- FILE HANDLING ---")

# Create & write file
with open("sample.txt", "w") as f:
    f.write("Hello Om!\nWelcome to Python.\nThis is Day 12 code.")

# Read file
with open("sample.txt", "r") as f:
    content = f.read()

print("File Content:\n", content)


# -------------------------------
print("\n--- OOP (CLASS & OBJECT) ---")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Om", [90, 85, 95])
print("Student Name:", s1.name)
print("Average Marks:", s1.avg())


# -------------------------------
print("\n--- INHERITANCE ---")

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


# -------------------------------
print("\n--- ERROR HANDLING ---")

try:
    x = int("10")   # correct
    y = int("abc")  # error
except ValueError:
    print("Error: Cannot convert string to number!")


# -------------------------------
print("\n--- SIMPLE CALCULATOR ---")

def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid Operator"

print("10 + 20 =", calc(10, 20, "+"))
print("50 - 15 =", calc(50, 15, "-"))
print("6 * 7 =", calc(6, 7, "*"))
print("40 / 8 =", calc(40, 8, "/"))

print("\n--- PROGRAM END ---")
