#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr_dic = {}
    index_dic = {}
    for index, value in enumerate(arr):
        if not value == index + 1:
            arr_dic[value] = index
            index_dic[index] = value

    return_count = 0
    while True:
        # print("arr_dic is", arr_dic)
        if len(arr_dic) == 0:
            break
        for value, index in arr_dic.items():
            if value == index + 1:
                del arr_dic[value]
                del index_dic[index]
                break
            else:
                # print("value is", value)
                # print("index is", index)

                change_value = index_dic[value-1]
                change_index = arr_dic[change_value]
                # print("change_value is ", change_value)
                # print("change_index is ", change_index)

                arr_dic[value] = change_index
                arr_dic[change_value] = index
                index_dic[index] = change_value
                index_dic[change_index] = value
                return_count += 1
                # print("value is ", value)
                # print("arr_dic[value] is ", arr_dic[value])
                # print("return_count is", return_count)
                del arr_dic[value]
                del index_dic[change_index]

                break
    # print("return_count is" ,return_count)
    return return_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
