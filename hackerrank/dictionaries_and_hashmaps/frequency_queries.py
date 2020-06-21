#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    answer_list =[]
    q_dic = defaultdict(int)
    index_dic = defaultdict(int)
    
    for i in queries:
        if i[0] == 1:
            index_dic[q_dic[i[1]]] -= 1
            q_dic[i[1]] += 1
            index_dic[q_dic[i[1]]] += 1
        elif i[0] == 2:
            index_dic[q_dic[i[1]]] -= 1
            q_dic[i[1]] -= 1
            index_dic[q_dic[i[1]]] += 1

            if q_dic[i[1]] < 0:
                del q_dic[i[1]]
        else:
            if index_dic[i[1]] >= 1:
                answer_list.append(1)
            else:
                answer_list.append(0)
        
    return answer_list
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
