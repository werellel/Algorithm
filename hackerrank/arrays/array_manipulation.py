#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def naive_arrayManipulation(n, queries):
    return_list = [0]*n
    for query in queries:
        for i in range(query[0]-1, query[1]):
            return_list[i] += query[2]
    return max(return_list)

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l = [0]*(n+1)
    for a, b, k in queries:
        l[a-1] += k
        l[b] -= k;
    max_value = a = 0
    for i in l:
       a+=i;
       if max_value<a:
            max_value=a;
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
