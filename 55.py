# AIM: To understand the concept of mutable (set) and immutable (frozenset) data structures in Python.

# --- Mutable Set Example ---
print("🔹 Mutable Set Example:")
my_set = {1, 2, 3, 4}
print("Original Set:", my_set)

# You can add or remove elements (mutable)
my_set.add(5)
print("After Adding 5:", my_set)

my_set.remove(2)
print("After Removing 2:", my_set)

# --- Immutable Frozenset Example ---
print("\n🔹 Immutable Frozenset Example:")
my_frozenset = frozenset([1, 2, 3, 4])
print("Original Frozenset:", my_frozenset)

# Trying to modify will cause an error
try:
    my_frozenset.add(5)
except AttributeError:
    print("❌ Error: Cannot modify frozenset (immutable)")

# --- Common Set Operations (work on both) ---
set_a = {1, 2, 3}
set_b = {3, 4, 5}
fset_a = frozenset([1, 2, 3])
fset_b = frozenset([3, 4, 5])

print("\nUnion of sets:", set_a | set_b)
print("Intersection of frozensets:", fset_a & fset_b)