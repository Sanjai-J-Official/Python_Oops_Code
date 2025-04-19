class demo:
    
    a=10
    b=20
    c=30
 
obj1=demo()
obj2=demo()
demo.d=100
 
print(obj1.a,id(obj1.a))
obj1.a=obj1.a+10
print(id(demo.a))
print(obj1.a,id(obj1.a)) 

