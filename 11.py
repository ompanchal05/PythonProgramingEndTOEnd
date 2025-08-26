#3 Lopping 

# for loop 
for ch in "abc":
    print(ch)

# while loop
i = 0
while i < 3:
    print(i)
    i += 1

#range & enumerate 
for i , val in enumerate ([10,20,30]):
    print(i , val)

#break , continue ,else 
for n in range (2,10):
    if n % 7 == 0:
        print("Found:" , n)
        break
    else :
         print("No Multiple of 7")