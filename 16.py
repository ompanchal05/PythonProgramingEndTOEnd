#8 Global and NoLocal

count = 0

def inc ():
    global count 
    count += 1 
inc ()
print(count)