#2. Accept Comma-Separated Numbers and Generate List & Tuple

# Take input from user
numbers = input("Enter comma-separated numbers: ")

# Split input string into list
list_numbers = numbers.split(",")

# Convert list to tuple
tuple_numbers = tuple(list_numbers)

print("List:", list_numbers)
print("Tuple:", tuple_numbers)
