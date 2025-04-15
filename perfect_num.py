n=6
i=1
s=[]
while i<n:
    if n%i==0:
        s.append(i)
    i+=1
if sum(s)==n:
    print("Perfect Number")
else:
    print("Not perfect Number")
