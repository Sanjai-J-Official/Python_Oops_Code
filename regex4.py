import re

txt='This is Python Code'

x=re.sub("\s",'__',txt,2)
print(x)