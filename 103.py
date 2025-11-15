# Safe Calculator
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        print("Result:", a / b)
    else:
        print("Invalid choice!")

except ValueError:
    print("Please enter numeric values only!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
