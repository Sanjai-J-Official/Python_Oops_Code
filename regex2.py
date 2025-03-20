import re

txt='This is Python Find the is value then length of is'
x=re.findall('is',txt)
print(len(x))