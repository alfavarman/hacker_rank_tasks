import re

# t1 = '11:22:43PM'
# print(t1[1] != '2')
# # print(int(t1[:2]))
# # print((str(int(t1[:2])+12))+(t1[2:]))
#
# The aim should never been said.
# the number 123 is less than055
# even decimal 0.66
# ABCDEFGHIJKLMNOPRSTUWVQXYZ
content = """abcdefghijklmnoprstuwvxyz

numbers:
888.222.3337
323-323-5347
239rjd90    09
niddniInnisnisINinsi
'S;M;thisIsAMethod()'
inputSample1 = 'C;M;this is a method'
inputSample2 = 'C;V;this is a variable'
inputSample3 = 'S;V;thisIsAVariable'
inputSample4 = 'S;C;ThisIsAClass'
inputSample5 = 'C;C;this is a class'
"""

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(content)

for match in matches:
    print(match)
