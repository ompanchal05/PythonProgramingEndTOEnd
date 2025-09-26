# WAP To Print the Number of the Even with Function and odd with Class ?

# Function to print even numbers
def print_even_numbers(limit):
    print("Even Numbers:")
    for i in range(1, limit + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print("\n")  


# Class to print odd numbers
class OddNumbers:
    def __init__(self, limit):
        self.limit = limit

    def print_odd_numbers(self):
        print("Odd Numbers:")
        for i in range(1, self.limit + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print("\n")  


# ---- Main Program ----
n = int(input("Enter the limit: "))

# Using function
print_even_numbers(n)

# Using class
odd = OddNumbers(n)
odd.print_odd_numbers()
