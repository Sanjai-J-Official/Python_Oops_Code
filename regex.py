import re
st='This is python Code'
x=re.search('^is.*Code$',st)

if x:
    print("Yes it is Match")
else:
    print("No Nothing can match!")
