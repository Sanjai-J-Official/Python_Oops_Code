lis=[11,14,15,2,30,2,23,4,1,3]
lis2=[2,3,4,6,6,5,4,4,3,7]
lis3=[1,2,3,4,5]
students=[("sanjai",22),("jai",19),("Hari",21),("Siva",34)]
veg=["carrot","mango","potato","tomato","chilly",'sdedsf']
s=map(lambda s: s**2,lis)
s1=map(lambda a,b: a**b,lis,lis2)
s2=filter(lambda x: x%2==0,lis)
s3=sorted(lis3,reverse=False)
s4=sorted(lis,key=lambda x : x)
s5=sorted(students,key=lambda x: x[1])
s6=sorted(veg)
s7=max(veg,key=len)

print(list(s))
print(min(list(s1)))
print(max(list(s2)))
print(len(list(s4)))
print(s5[2])
print(list(s3))
print(sum(list(s3),12))

print(s6)
print(s7) 