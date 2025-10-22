# Aim: To reverse a string and convert it into a number

# Input a string (number in string form)
s = input("Enter a number in string form: ")

# Reverse the string
reversed_str = s[::-1]

# Convert the reversed string into an integer
reversed_num = int(reversed_str)

# Display results
print("Original string:", s)
print("Reversed string:", reversed_str)
print("Reversed number:", reversed_num)
