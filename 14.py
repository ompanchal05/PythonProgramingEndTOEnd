#6 Functions 

def greet (name = "World"):
    return f"Hello,{name}!"
print (greet ("OM"))
print(greet())

#args & Kwargs 

def demo (a, b=0, *args , c=1 , **kw):
    return a,b,args , c, kw
print(demo (10,20,30,40,c=99,x=99))
