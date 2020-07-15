#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    l_count = 0
    h_count = 0
    i = 0
    for i in range(len(scores)):
        if i == 0:
            ls = scores[0]
            hs = scores[0]
            i = i + 1
        elif scores[i] < ls:
            ls = scores[i]
            l_count = l_count + 1
            i = i + 1
        elif scores[i] > hs:
            hs = scores[i]
            h_count = h_count + 1
            i = i + 1
    return h_count,l_count





    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
