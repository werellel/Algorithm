#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    return_value = 0
    a_dic = collections.Counter(a)
    b_dic = collections.Counter(b)
    for key, a_value in a_dic.items():
        if a_value != b_dic[key]:
            diff_value = a_value - b_dic[key]
            return_value += abs(diff_value)
            a_dic[key] -= diff_value
    
    for key, b_value in b_dic.items():
        a_value = a_dic[key]
        if b_value != a_value:
            return_value += b_value

    return return_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
