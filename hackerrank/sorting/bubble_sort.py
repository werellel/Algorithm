#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swap_count = 0
    for idx1, num1 in enumerate(a):
        for idx2, num2 in enumerate(a[:-1]):
            if a[idx2] > a[idx2+1]:
                temp_val = a[idx2]
                a[idx2] = a[idx2+1]
                a[idx2+1] = temp_val
                swap_count += 1
    print("Array is sorted in %s swaps." %(str(swap_count)))  
    print("First Element: %s"%(str(a[0])))  
    print("Last Element: %s"%(str(a[-1])))  
    return

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
