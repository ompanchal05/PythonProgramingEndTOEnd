# AIM: To reverse a string, number, and list in Python

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to reverse a number
def reverse_number(n):
    return int(str(n)[::-1])

# Function to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Main Program
if __name__ == "__main__":
    # Reverse a string
    string_input = "HELLO WORLD"
    print("Original String:", string_input)
    print("Reversed String:", reverse_string(string_input))
    print("-" * 40)
    
    # Reverse a number
    number_input = 12345
    print("Original Number:", number_input)
    print("Reversed Number:", reverse_number(number_input))
    print("-" * 40)
    
    # Reverse a list
    list_input = [10, 20, 30, 40, 50]
    print("Original List:", list_input)
    print("Reversed List:", reverse_list(list_input))
