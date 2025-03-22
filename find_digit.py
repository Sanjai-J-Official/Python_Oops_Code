import re

txt='This string to find the all digits like 3 now print the 23 '

x=re.findall('\d',txt)

print(x)