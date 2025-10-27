#Note 1: Starting today, I’ll be focusing on Python basics since my exams have begun. This will help maintain consistent GitHub activity while revising core concepts.

#Note 2: This approach will be helpful for both of us in reinforcing the fundamentals.

# AIM : To understand and demonstrate the working of arrays in Python, including basic operations like creation, traversal, insertion, updating, and deletion.

# Importing the array module
from array import array

# Creating an integer array
arr = array('i', [10, 20, 30, 40, 50])
print("Original Array:", arr.tolist())

# Accessing elements
print("First Element:", arr[0])
print("Last Element:", arr[-1])

# Inserting an element
arr.insert(2, 25)
print("After Insertion:", arr.tolist())

# Updating an element
arr[3] = 35
print("After Updation:", arr.tolist())

# Deleting an element
arr.remove(50)
print("After Deletion:", arr.tolist())

# Traversing (Loop through the array)
print("Traversing Array Elements:")
for i in arr:
    print(i, end=" ")