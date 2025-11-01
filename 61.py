#WAP For the making list to tuple and mutabble to immutable 

# AIM: To understand conversion of a mutable list into an immutable tuple

# Creating a list (mutable)
my_list = [10, 20, 30, 40]

print("Original List:", my_list)

# Modifying the list (allowed)
my_list.append(50)
print("Modified List:", my_list)

# Converting list to tuple (immutable)
my_tuple = tuple(my_list)
print("Converted Tuple:", my_tuple)

# Trying to modify tuple (not allowed)
try:
    my_tuple[0] = 100
except TypeError:
    print(" Error: Tuple is immutable, cannot modify its elements!")
