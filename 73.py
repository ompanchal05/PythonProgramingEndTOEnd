# 1.Program to Calculate the Number of Days Between Two Dates

from datetime import date
# Input two dates (year, month, day)
date1 = date(2025, 11, 1)
date2 = date(2025, 11, 7)

# Calculate difference
delta = date2 - date1

print("Number of days between dates:", delta.days)