import re

txt="Hello World"

x=re.findall("He.{3}",txt)
print(x)