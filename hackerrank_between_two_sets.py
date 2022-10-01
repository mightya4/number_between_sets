#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    tempA = a
    tempB = b
    startPoint = max(a)
    endPoint = min(b)
    arrayOfFactors = []
    removed_list = []
 
    for num in range(startPoint, endPoint + 1):
        arrayOfFactors.append(num)
    for tempNum in tempA:
        for currentNum in arrayOfFactors:
            if currentNum % tempNum != 0:
                removed_list.append(currentNum)
    
    
    for tempNum in tempB:
        for currentNum in arrayOfFactors:
            if tempNum % currentNum !=0:
                removed_list.append(currentNum)

    removed_list = list(set(removed_list))
    
    arrayOfFactors = [x for x in arrayOfFactors if x not in removed_list]
    return len(arrayOfFactors)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
