import re

txt="this is find the digits in the string for example : 7436,12357 extarct the data in the string"

x=re.findall(r"\d",txt) #if \d is use to find digits in the string seprately
y=re.findall(r"7436",txt) #also we use direct string 

print(x)
print(y)