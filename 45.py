# Give the program of the Regular Expressions – REs,

# Regular Expressions in Python
import re

# Sample text
text = "My email is om123@gmail.com and phone number is 9876543210. I live in Ahmedabad."

# 1. Search for an email pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = re.findall(email_pattern, text)
print("Email Found:", email)

# 2. Search for a phone number (10 digits)
phone_pattern = r'\b\d{10}\b'
phone = re.findall(phone_pattern, text)
print("Phone Number Found:", phone)

# 3. Check if a string starts with "My"
if re.match(r'^My', text):
    print("The string starts with 'My'.")

# 4. Replace text using re.sub()
new_text = re.sub(r'Ahmedabad', 'Mumbai', text)
print("After Replacement:", new_text)

# 5. Split text by spaces or punctuation
split_text = re.split(r'[ ,.]', text)
print("Splitted Words:", [word for word in split_text if word])  # remove empty strings
