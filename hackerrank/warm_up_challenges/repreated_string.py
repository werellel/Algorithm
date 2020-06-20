#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_s = len(s)
    a_c = s.count('a')
    rotate_count = n // len_s
    mod = n % len_s
    
    return (a_c * rotate_count) + s[:mod].count('a')
