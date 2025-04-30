lis=[23,54,21,10,9]
s,m=lis[0],lis[0]
print("first:",s,m)
for i in lis:
    print("------")
    if i>m:
        m=i
        print("m:",m)
    if i<s:
        s=i
        print("s:",s)

print("max:",m)
print('min:',s)