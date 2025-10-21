#Advance Topic of python #2

#To demonstrate the working of Python’s defaultdict.

from collections import defaultdict

marks  = defaultdict(int)

marks['Om'] = 10
marks['Praveen'] = 5

print ("student marks recoed:")
print("dict(marks)")

print("\n Accesing missing key Shrey:", marks['Shrey'])
print("Updated dictionary after accessing missing key:")
print(dict(marks))
