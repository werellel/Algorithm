#!/bin/python3
# url:https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    count = 0
    index = 0
    while True:
        print(index)
        if index >= n - 3:
            break
        if 1 in c[index:index+2]:
            index += 2
            count += 1
        elif 1 == c[index+2]:
            index += 3
            count += 2
        else:
            index += 2 
            count += 1
    if index < n -1:
        count += 1
    return count 

if __name__ == '__main__':
    c = [0, 1, 0]
    print(jumpingOnClouds(c))