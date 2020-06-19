#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_dic = {}
        
    for sock in ar:
        get_sock = sock_dic.get(sock, None)
        if get_sock == None:
            sock_dic[sock] = 1
        else:
            sock_dic[sock] += 1
    return_value = 0
    for key, value in sock_dic.items():
        return_value += value // 2
    
    return return_value