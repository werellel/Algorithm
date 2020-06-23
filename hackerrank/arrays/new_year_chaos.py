#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    move = 0
    for idx, num in enumerate(q):
        if num - (idx+1) > 2:
            return 'Too chaotic'
        
        for idx2 in range(max(num-2,0), idx):
            if q[idx2] > num:
                move += 1
    return move
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    move = 0
    for idx, num in enumerate(q):
        if num - (idx+1) > 2:
            return 'Too chaotic'
        
        for idx2 in range(max(num-2,0), idx):
            if q[idx2] > num:
                move += 1
    return move
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
