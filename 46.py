#WAP for pelidrome 

# Simple palindrome check (exact match)
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
