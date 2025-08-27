#5 Iteration & Comprehensions 

#Iterator 
it = iter ([1,2,3])
print(next(it))

# List comprehension
squares = [x*x for x in range(5)]
print(squares)

#Set Comprehension 
evens = {x for x in range (10) if x%2 == 0}
print(evens)

#Dict Comprehension 
lengths = {w: len(w) for w in ["Hi", "Hello"]}
print(lengths)