import re

txt="th+is7 3435 sdofi asA12oo04oSkki04wnd"

not_digit=re.findall("\D",txt)
white_space=re.findall("\s",txt)
not_white_space=re.findall("\S",txt)
every_char=re.findall("\w",txt)
not_char=re.findall("\W",txt)
find_char=re.findall("[is]",txt)
particular_char=re.findall("[a-n]",txt)
except_particular_char=re.findall("[^a-n]",txt)
digit_find=re.findall('[0123]',txt)
digit_between=re.findall('[5-7]',txt)
two_digit_find=re.findall("[0][4]",txt)
case_alphabet=re.findall("[A-Z]",txt)
symbol_find=re.findall('[+]',txt)
first_white_space_index=re.search('\s',txt)
split_txt=re.split('\s',txt,2)
split1_txt=re.split('s',txt,3)
replace_txt=re.sub('\s','9',txt)
replace_txt2=re.sub('\s','9',txt,2)

print(not_digit,white_space,not_white_space,every_char,not_char,find_char,particular_char,sep='\n')
print(except_particular_char,digit_find,digit_between,two_digit_find,case_alphabet,symbol_find, sep='\n')
print(first_white_space_index.start(),split_txt,split1_txt,replace_txt,replace_txt2,sep='\n')
