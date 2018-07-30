#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aliceCount=0
    bobCount=0

    for i in range(3):
        if a[i] > b[i]:
            aliceCount+=1
        elif a[i] < b[i]:
            bobCount+=1

    return aliceCount, bobCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
