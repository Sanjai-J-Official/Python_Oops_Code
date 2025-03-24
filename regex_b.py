import re

txt="starting the string itsnotstartand itsend tonotending of code also have center the string "

a=re.findall(r"\bstart",txt) #if \b is start to use find the pattern in Begining of word
b=re.findall(r"end\b",txt) #if \b is end to use find the pattern in end of Word

x=re.findall(r"\Bnotstart",txt) #if \B is  start  to use find Pattern But NOT in Begining either Center or Ending  of words
y=re.findall(r"notend\B",txt) #if \B is end to use find the pattern But not in Ending either Center or Starting

print(a)
print(b)
print(x)
print(y)