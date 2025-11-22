import re

email = input("Enter email: ")

pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+"

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
