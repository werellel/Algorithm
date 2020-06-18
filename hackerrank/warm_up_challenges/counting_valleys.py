#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    if s[0] == 'U':
        result_list = [(0, '_')]
        compare_pos = -1
    
    else:
        result_list = [(1, '_')]
        compare_pos = 0
    
    
    position = 0
    change = '-'
    p_max = 0
    p_min = 0
    valley_count = 0
    for i in s:
        if i == 'U':
            if i == change:
                position += 1
            else:
                change = i

            if position == compare_pos:
                valley_count += 1

            result_list.append((position, '/'))

        else:
            if i == change:
                position -= 1
            else:
                change = i
                
            result_list.append((position, '\\'))

        if position > p_max:
            p_max = position

        if position < p_min:
            p_min = position
    
    return valley_count

if __name__ == '__main__':
    n = 8
    s = 'UDDDUDUU'
    result = countingValleys(n, s)
    print(result)

# Visualize the countingValleys
def visualize_countingValleys(n, s):
    if s[0] == 'U':
        result_list = [(0, '_')]
        compare_pos = -1
    
    else:
        result_list = [(1, '_')]
        compare_pos = 0
    position = 0
    change = '-'
    p_max = 0
    p_min = 0
    valley_count = 0
    for i in s:
        if i == 'U':
            if i == change:
                position += 1
            else:
                change = i
            if position == compare_pos:
                valley_count += 1

            result_list.append((position, '/'))
        else:
            if i == change:
                position -= 1
            else:
                change = i
                
            result_list.append((position, '\\'))
        if position > p_max:
            p_max = position
        if position < p_min:
            p_min = position
    if s[-1] == 'U':
        result_list.append((0, '_'))
    else:
        result_list.append((1, '_'))
    
    str_list = [' '*(n+2) for i in range(p_max-p_min+1)]
    for index, row in enumerate(result_list):
        str_list[p_max - row[0]] = str_list[p_max - row[0]][:index] + row[1] + str_list[p_max - row[0]][index+1:]
    result = ''
    for i in str_list:
        result = result + i + '\n'
    return result
