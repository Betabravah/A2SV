#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] > arr[j-1]:
                pass
            else:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        for i in arr:
            print(i, end = " ")
        print("")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
