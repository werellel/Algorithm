#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the isValid function below.
def isValid(s):
    remove_time = 0
    s_dic = collections.Counter(s)
    temp_value = s_dic[s[0]]
    for key, value in s_dic.items():
        if abs(temp_value - value) >= 1:
            remove_time += 1
            if remove_time >= 2:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
