"""
given an array return the index i when the sum reached the target or a higher number
ex: [ 300 200 100 200 500 ] target = 700

i = 0, sum = 300
i = 1, sum = 500
i = 2, sum = 600
i = 3, sum = 800

800 >= 700 so return 3
return -1 if nothing found
"""

from typing import List


def solution(visits: List[int], target: int):

    if len(visits) == 0:
        return -1
    
    if len(visits) == 1 and visits[0] == target:
        return 0

    currentSum = 0

    for i in range(len(visits)):
        currentSum += visits[i]

        if currentSum >= target:
            return i
        
    return -1

    
