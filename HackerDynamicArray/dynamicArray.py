#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):

    # Write your code here
    arr = []
    for i in range(n):
        arr.append([])
    
    ans = []
    lastAnswer = 0
    
    for query in queries:
        x = query[1]
        
        # always make sure the computed index stays in range of arr length
        idx = (x ^ lastAnswer) % len(arr)
        
        y = query[2]
        
        if query[0] == 1:
            arr[idx].append(y)   
        else:
            lastAnswer = arr[idx][y%len(arr[idx])]
            ans.append(lastAnswer)
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
