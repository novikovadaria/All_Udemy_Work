import re


test_string = 'ten'
test_string = 'cat'
test_string = 'dog'  # dont match
pattern = '.e.'
result = re.match(pattern, test_string)
print(result)


# [] Square brackets
match_result = re.finditer('[abc]', 'a')
match_result = re.finditer('[a-e]', 'dog frog dream')
for match in match_result:
    print(match)

#  not in []
match_result = re.finditer('[^abc]', 'dog frog dream')
for match in match_result:
    print(match)


# Period
match_res = re.finditer('.', '123')
match_res = re.finditer('..', '123')  # two that are next to each other
for match in match_res:
    print(match)


# ^ Caret
match = re.finditer('^a', 'a')  # if the string starts with a char
for match in match:
    print(match)


# $
m_r = re.finditer('$a', 'a')  # whether it ends or not

# *
match_r = re.finditer('ma*n', 'mn')
for match in match_r:
    print(match)


# +
match_result = re.finditer('ma+n', 'mn')
match_result = re.finditer('ma+n', 'man')
for match in match_result:
    print(match)


# ?
match_result = re.finditer('ma?n', 'man')
for match in match_result:
    print(match)


# {}
match_result = re.finditer('a{2,4}', 'abc dat')
for match in match_result:
    print(match)


match_result = re.finditer('[0-9]{2,4}', 'abc 123 def ghi 45')
for match in match_result:
    print(match)

# Alternation
match_result = re.finditer('a|b', 'adc')
match_result = re.finditer('z|c', 'adc')
match_result = re.finditer('c|z|t', 'zzc')
for match in match_result:
    print(match)


# Group
match_result = re.finditer('(a|b)xz', 'abc xz')
match_result = re.finditer('(a|b)xz', 'abcxz')
for match in match_result:
    print(match)


# \
match_result = re.finditer('\^xz', '^xz')
for match in match_result:
    print(match)


# ....................Methods..............
# \d
# findall()
string = 'hello 12 hi 65 123 howdy 784 907'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)

# split()
string = 'hello 12 hi 65 123 howdy 784 907'
pattern = '\d+'
result = re.split(pattern, string)
print(result)

# sub()
# (patter, replace, string)
string = 'abc 12\ de 23 \n f45 621'
patter = '\s+'
print(re.findall(patter, string))
replace = ''
new_string = re.sub(pattern, replace, string)
print(new_string)

# sub()
string = 'abc 12 de 23 \n f45 621'
patter = '\s+'
new_string = re.sub(pattern, replace, string, 1)
print(new_string)

# subn()
string = 'abc 12 de 23 \n f45 621'
patter = '\s+'
replace = ''
new_string = re.sub(pattern, replace, string, 1)
print(new_string)

# search()
stribg = 'python is fun'
patter = '\Apython'
match_result = re.search(patter, string)
print(match_result)


# match.group()
string = '12345 67, 7894 1122'
pattern = r'(\d{3}) (\d{2})'
match = re.search(pattern, string)
if match:
    print(match.group())
else:
    print('match not found')


# ..........................Raw string.......................
string = '\tBook'
print(string)
string = r'\tBook'
print(string)

# ....................Speacial sequences...............
# \d [0-9]
# \D [a-zA-Z] + symbols ans spaces
# \S [a-zA-Z0-9]
# \w [a-zA-Z0-9_] # alphanumer
# \W -not [a-zA-Z0-9_] # alphanumer
# \b  in the end  and in the begining
# \B not at the begining and not at the begining
