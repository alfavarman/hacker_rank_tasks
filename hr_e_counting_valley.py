#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

path = "DDDUUUUUDDDDDDUDUDUUUU"
steps_n = len(path)

def countingValleys(steps: int, path: str) -> int:
    # Write your code here
    passed_valleys_counter = 0
    steps_list = list(path)
    latitude = 0
    for step in steps_list:
        if step == "D":
            latitude -= 1
        if step == "U":
            latitude += 1
            if latitude == 0:
                passed_valleys_counter += 1

    return passed_valleys_counter


print(countingValleys(steps_n, path))
