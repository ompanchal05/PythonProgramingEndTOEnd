# AIM : To understand and demonstrate the use of the Counter class from Python’s collections module, which helps count the frequency of elements in an iterable (like lists or strings).

from collections import Counter

# Count frequency of elements
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)

print(counter)
print(counter.most_common(2))  # Top 2 items
