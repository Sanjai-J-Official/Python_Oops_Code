#print middle char of the str if its uppercase 
n=input("Enter the String:")
if type(n)==str:
    if len(n)%2!=0:
        mid=n[len(n)//2]
        if 'A'<=mid<='Z':
            print(f"middle value:",mid)
        else:
            print("Not Uppercase")
    else:
        print("Not Middle value")