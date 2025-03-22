import re
n=input("enter the String:")
txt='Hello Python!'

x=re.findall(f'^{n}',txt)
if x:
    print(f"Yes {n} is Starting")
else:
    print("No Your input is Not Starting String")