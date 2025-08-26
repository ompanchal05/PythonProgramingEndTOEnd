#4 String & Input 

s = "Python"
print(s[0],s[-1]) 
print(s[1:4])

#String Methods

print(s.upper())
print(s.replace("Py", "My"))

#concatenation & split/join 

msg = "Hello ," + "Om"
print(msg)
print("-".join(["a","b","c"]))
print("ab,cd,ef".split(","))

#f-string
score = 95
print(f"{msg}scored{score}")