import math
import os
import random
import re
import sys


13
strings_ar = ['abcde',
'sdaklfj',
'asdjf',
'na',
'basdn',
'sdaklfj',
'asdjf',
'na',
'asdjf',
'na',
'basdn',
'sdaklfj',
'asdjf']
5
queries1 = ['abcde',
'sdaklfj',
'asdjf',
'na',
'basdn']
#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for i in queries:
        result.append(strings.count(i))
    return result

print(matchingStrings(strings_ar, queries1))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     strings_count = int(input().strip())
#
#     strings = []
#
#     for _ in range(strings_count):
#         strings_item = input()
#         strings.append(strings_item)
#
#     queries_count = int(input().strip())
#
#     queries = []
#
#     for _ in range(queries_count):
#         queries_item = input()
#         queries.append(queries_item)
#
#     res = matchingStrings(strings, queries)
#
#     fptr.write('\n'.join(map(str, res)))
#     fptr.write('\n')
#
#     fptr.close()