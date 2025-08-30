#Function with data structure and find the even or odd 

def check_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return {
        "Even Numbers": even_numbers,
        "Odd Numbers": odd_numbers
    }
data = [10,15,22,33,42,55,66]
result = check_even_odd(data) 

print("Input List:", data)
print("Even Numbers:", result["Even Numbers"])
print("Odd Numbers:", result["Odd Numbers"])
