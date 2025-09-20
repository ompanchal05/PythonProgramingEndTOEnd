#In Python using re (regular expressions module) with all the common functions and examples.
#4 CODES TO EXPLAINS ALL OF THIS 

import re

text = "apple is tasty"
match = re.match(r"apple", text)
if match:
    print("Match found:", match.group())
text = "I like apples and bananas"

#OUT PUT 1 : APPLE FOUND 

search = re.search(r"bananas", text)
if search:
    print("Found:", search.group())

# OUT PUT 2 : BANANAS FOUND 

text = "cat bat mat rat"

words = re.findall(r"\b\w{3}\b", text)  # All 3-letter words
print("Words:", words)

#OUTPUT 3 : Words: ['cat', 'bat', 'mat', 'rat']

text = "123 456 789"

for match in re.finditer(r"\d+", text):
    print("Match:", match.group(), "at position:", match.span())

# OUT PUT 4 : Match: 123 at position: (0, 3)
#Match: 456 at position: (4, 7)
#Match: 789 at position: (8, 11)
