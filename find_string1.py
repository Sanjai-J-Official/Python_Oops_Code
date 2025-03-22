import re

txt="This is Hello World oral text"
x=re.findall("He.+o",txt)
print(x)