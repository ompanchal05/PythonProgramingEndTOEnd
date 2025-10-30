#Test 2
#Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers. 


# Accept a sequence of comma-separated numbers from the user
numbers = input("Enter comma-separated numbers: ")

# Split the input string into a list
list_numbers = numbers.split(",")

# Convert the list into a tuple
tuple_numbers = tuple(list_numbers)

# Display the results
print("List:", list_numbers)
print("Tuple:", tuple_numbers)
