#Python Code to Find Factorial of a Number

# Program to find factorial of a number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)
