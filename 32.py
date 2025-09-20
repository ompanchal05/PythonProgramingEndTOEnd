# Write a regular expression to retrieve all words having 5 character length

import re 
  
text = "Hello world, apple mango tiger stone beard happy"

words = re.findall(r'\b\w{5}\b', text)

print ("Words with 5 characters:", words)