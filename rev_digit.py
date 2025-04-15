i=11234

sum=0
while i>0:
    ld=i%10
      
    sum=sum*10+ld  
    i=i//10
      
print(sum)