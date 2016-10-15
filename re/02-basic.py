import re

# print re.split(r'\s*', 'here are some words')  # \s = space character  # * = any amount
#
# print re.split(r'(\s*)', 'here are some words')  # () = group and include argument in list
#
# print re.split(r'(s*)', 'here are some words')  # s* = evaluates s as a char
#
# print re.split(r'[a-f]', 'ksdjfdosifudshwennqqps')  # [a-f] = retrieve range of char
#
# print re.split(r'[a-fA-F0-9e-q]', 'ldsjflsjslf')  # [a-fA-F0-9e-q] = multi-range
#




# Flags
# print re.split(r'[a-f]', 'ksdjfdosifudshwennqqps', re.I | re.M)  # re.I = ignore caps  # re.M = search multi-line

# --- findall --- #
print re.findall(r'\d', 'here321 main st.dsfd')  # \d = digits
print re.findall(r'\D', 'here321 main st.dsfd')  # \d = digits


# --- groupers --- #
print re.findall(r'\d*', 'here321 main st.dsfd')  # * = find all
print re.findall(r'\d+', 'here321 main st.dsfd')  # + = one or more
print re.findall(r'\d?', 'here321 main st.dsfd')  # ? = only 0 or 1
print re.findall(r'\d{1,5}', 'here321 main st.dsfd')  # {1,5} = range
print re.findall(r'\d\w', 'here321 main st.dsfd')  # w = only number or letter
print re.findall(r'\d\.', 'here321 main st.dsfd')  # . = anything



# --- Examples --- #
print re.findall(r'\d{1,5}\s\w+\s\w+\.', 'here321 main st.dsfd')  # w = only number or letter