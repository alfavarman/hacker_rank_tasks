#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts following parameters:
n1 = 6 #  1. INTEGER n
k1 = 3 #  2. INTEGER k
arr1 = [1, 3, 2, 6, 1, 2]#  3. INTEGER_ARRAY ar


def divisibleSumPairs(n: int = n1, k: int = k1, arr: list = arr1) -> int:
    result = 0
    for i in range(n1):
        for j in range(1, n1):
            if i < j:
                suma_ij = (arr[i] + arr[j])
                if suma_ij % k == 0:
                    result += 1
    return result


print(divisibleSumPairs())
    # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     first_multiple_input = input().rstrip().split()
#
#     n = int(first_multiple_input[0])
#
#     k = int(first_multiple_input[1])
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = divisibleSumPairs(n, k, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()