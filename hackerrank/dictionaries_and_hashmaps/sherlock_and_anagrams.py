#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from math import factorial

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    a_z_dic = defaultdict(int)
    for index, word in enumerate(s):
        for index2, word2 in enumerate(s[index:]):
            sorted_data = sorted(s[index:index2+index+1])
            a_z_dic[str(sorted_data)] += 1
    answer = 0
    for key, value in a_z_dic.items():
        if value <= 1:
            continue
        answer += factorial(value) / (factorial(value-2) * 2)
    return int(answer)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
