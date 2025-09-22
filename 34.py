# Use the pass by value and pass by refrance 

#Pass by value: -> Immutable

def change_number(x):
    print("Inside before:", x)
    x = x + 5     
    print("Inside after:", x)

num = 10
change_number(num)
print("Outside:", num)

#pass by refrance: -> Mutable

number = [1,2,3]

def list(lst):
    print("Inside before:" , lst)
    lst.append(4)
    print("Inside after:" , lst)

list(number)
print("Outside:",number)