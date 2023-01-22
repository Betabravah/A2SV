#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    ctr = 0
    for j in range (len(a) -1):
        for i in range (len(a) - 1):
            if a[i] > a[i+1]:
                a[i] , a[i+1] = a[i+1], a[i]
                ctr+=1
    print("Array is sorted in %d swaps."%ctr)
    print("First Element: %d"%a[0])
    print("Last Element: %d"%a[len(a)-1])
                
    
            
        
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
