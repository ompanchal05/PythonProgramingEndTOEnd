#Test 1
#Write a Python program to calculate the number of days between two dates. In Python

from datetime import date

# Input two dates (year, month, day)
year1, month1, day1 = map(int, input("Enter first date (YYYY MM DD): ").split())
year2, month2, day2 = map(int, input("Enter second date (YYYY MM DD): ").split())

# Create date objects
d1 = date(year1, month1, day1)
d2 = date(year2, month2, day2)

# Calculate difference
diff = abs((d2 - d1).days)

# Display result
print(f"The number of days between {d1} and {d2} is {diff} days.")
