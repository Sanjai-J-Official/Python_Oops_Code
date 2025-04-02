def binary(arr,tar):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        print("Mid value:",mid)
        if arr[mid]==tar:
            return mid
            
        elif arr[mid]<tar:
            left=mid+1
            print("left inc:",left)
        else:
            right=mid-1
            print("right icr:",right)
    else:
        return -1    
li=[]
for i in range(1,100000):
    li.append(i)
 
print(binary(li,99990))