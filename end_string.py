import re

txt="This is string to find hello world"

x=re.findall("d$",txt)
if x:
    print("End with string")
else:
    print("Not ends with")
