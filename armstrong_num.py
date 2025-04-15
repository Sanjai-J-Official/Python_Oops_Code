ran=400 
it=100
li=[]
while it <ran:
     
    org_n=it
    n=org_n
    i=n
    count=0
    while i>0:
        i=i//10
        
        count+=1 
 
    sum=0

    while n>0:
        ld=n%10
        sum+=ld**count
        n=n//10
    if it==sum:
        li.append(sum)    
    it+=1
print(li)

#spine snumber=  123   1*2*3=1+2+3

#perpect num=   6 multiples 1,2,3=add all =6


