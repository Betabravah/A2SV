#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    new_grades = []
   
    for i in grades:
        if i >= 38:
            for j in range (5):
                if ((i + j) % 5) == 0:
                    round = i +j
            if (round - i) < 3:
                i = round
        new_grades.append(i)
        
    return new_grades
                
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
