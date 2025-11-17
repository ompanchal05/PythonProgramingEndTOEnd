#Clean numeric data

data = ["10" , "20" , "30" , "abc" , "40"]

clean = [int(x) for x in data if x.isdigit()]
print(clean)

#Lambda with map(), filter(), reduce()

nums = [1,2,3,4,5,6]
square_nums = list(map(lambda x: x*x , nums))
print(square_nums)
evens = list(filter(lambda x: x%2 == 0, nums))
print(evens)

#reduce() -> cumlative result

from functools import reduce

nums = [1,2,3,4]
total = reduce(lambda a,b: a+b ,nums)
print(total)