import re

txt='This is Python Code'
x=re.search(r"\bP\w+",txt)
print(x.string)