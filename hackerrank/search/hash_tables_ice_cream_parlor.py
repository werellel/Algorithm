#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    m_dic = {}
    for index, i in enumerate(cost):
        if m_dic.get(i, None) == None:
            m_dic[i] = [index+1]
        else:
            m_dic[i].append(index+1)

    for key, value in m_dic.items():
        if money-key == key:
            if len(m_dic[key]) >= 2:
                m_dic[key].sort(reverse=True)
                print(m_dic[key].pop(), m_dic[key].pop())
                return 

        elif money-key in m_dic:
            return_list = [m_dic[money-key].pop(), m_dic[key].pop()]
            return_list.sort(reverse=True)
            print(return_list.pop(), return_list.pop())
            return
        else:
            pass
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
