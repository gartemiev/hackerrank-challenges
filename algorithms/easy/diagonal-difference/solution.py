#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diagonalOne=sum([arr[i][i] for i in range(len(arr[0]))])
    diagonalTwo=sum([arr[i][j] for i,j in zip(range(len(arr[0])),reversed(range(len(arr[0]))))])

    return abs(diagonalOne - diagonalTwo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
