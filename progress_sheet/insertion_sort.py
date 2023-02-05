#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    right = n - 1
    for i in range(n-1, -1, -1):
        if arr[i] > arr[right]:
            temp = arr[right]
            arr[right] = arr[i]
            print(*arr)
            arr[i] = temp
            right -= 1
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
