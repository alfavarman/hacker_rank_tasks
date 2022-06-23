# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# Example
#
#
# Return '12:01:00'.
#
#
# Return '00:01:00'.
#
# Function Description
#
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#
# timeConversion has the following parameter(s):
#
# string s: a time in  hour format
# Returns
#
# string: the time in  hour format
# Input Format
#
# A single string  that represents a time in -hour clock format (i.e.:  or ).
#
# Constraints
#
# All input times are valid
# Sample Input
#
# 07:05:45PM
# Sample Output
#
# 19:05:45
import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def time_conversion(time_str: str) -> str:
    """function return time in 24h format

    :param time_str: str time representation in hh:mm:ssA/PM
    :return:str time in hh:mm:ss
    """

    global time_converted

    time_converted = time_str
    # if time is PM and hours is not 12 than its hours increased of 12
    if time_str[-2] == 'P': # one line AND statement
        if time_str[0:2] != '12':
            # for str(int(sliced hours)+12) and add rest of str
            time_converted = (str(int(time_str[:2])+12))+(time_str[2:])

    else:
        # for am only change 12 to 00
        if time_str[0:2] == '12':
            time_converted = (str('00' + (time_str[2:])))
    time_converted = time_converted[:-2]
    return time_converted


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = timeConversion(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()


# print(time_conversion('12:44:59PM'))
# time_str = '12:44:59PM'
# print(time_str[1] == '2')
time_l = ['12:22:43AM', '02:44:59AM', '12:22:43PM', '02:22:43PM'] #'10:35:01AM', '11:22:43PM', '05:22:43PM',
          # '11:22:43PM', '05:59:59AM', '11:59:59PM', '12:00:01AM', '12:00:00PM', '10:35:01AM', '04:35:01AM',
          # '10:22:43PM', '04:22:43PM', '11:22:43PM', '12:22:43AM', '10:35:01AM', '09:22:43PM', '03:22:43PM',
          # '09:22:43PM', '02:59:59AM', '11:59:59PM', '12:00:01AM', '12:00:00PM', '08:35:01AM', '02:35:01AM',
          # '08:22:43PM', '02:59:59AM', '11:59:59PM', '12:00:01AM', '12:00:00PM', '07:35:01AM', '01:35:01AM',
          # '07:22:43PM', '11:59:59AM', '11:59:59PM', '12:00:01AM', '12:00:00PM', '06:35:01AM', '00:35:01AM']
for time in time_l:
    print(time + ' conversion ' + time_conversion(time))



