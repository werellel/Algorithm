#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    total_cnt = 0
    temp_same = 1
    for index, string in enumerate(s[:-1]):            
        if string == s[index+1]:
            temp_same += 1
        else:
            total_cnt += sum([i for i in range(1, temp_same+1)])
            temp_same = 1
    total_cnt += sum([i for i in range(1, temp_same+1)])
    
    total_cnt_2 = 0
    for index, string in enumerate(s):
        lens = 1
        while True:
            if index-lens < 0:
                break
            if index+1+lens > n:
                break
                
            if index+1 >= n:
                if s[index-lens:index] == s[index+1:] and s[index+1] != s[index]:
                    lens += 1
                else:
                    break
            else:
                if s[index-lens:index] == s[index+1:index+1+lens] and s[index+1] != s[index]:
                    lens += 1
                else:
                    break
        total_cnt_2 += lens -1
    return total_cnt + total_cnt_2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
