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
 
    for num in range(startPoint, endPoint + 1):
        arrayOfFactors.append(num)
    for tempNum in tempA:
        for currentNum in arrayOfFactors:
            if currentNum % tempNum != 0:
                print(f"{tempNum}%{currentNum} = {tempNum % currentNum}")
                if currentNum in arrayOfFactors:
                    arrayOfFactors.remove(currentNum)
    print(arrayOfFactors)
    
    for tempNum in tempB:
        for currentNum in arrayOfFactors:
            # print(f"{tempNum}%{currentNum} = {tempNum % currentNum}")
            if tempNum % currentNum !=0:
                if currentNum in arrayOfFactors:
                    arrayOfFactors.remove(currentNum)
    print(arrayOfFactors)
    return len(arrayOfFactors)


# a = [2, 4]
# b = [16, 32, 96]
# num = getTotalX(a, b)
# print(num)

a = [3, 4]
b = [24, 48]
num = getTotalX(a, b)
print(num)