a=[1,2,4,5,6,2,3]

 
s=list(set(a))
s.sort(reverse=True)

if len(s)>1:
    print(s[1])
else:
    None 

 
