#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m_dic = {}
    for i in magazine:
        if m_dic.get(i, None ) == None:
            m_dic[i] = 1
        else:
            m_dic[i] += 1
    n_dic = {}
    for i in note:
        if m_dic.get(i, None) == None:
            return 'No'
        else:
            get_data = m_dic.get(i)
            if get_data == 0:
                return 'No'
            else:
                 m_dic[i] -= 1
    return 'Yes'
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
