
"""
count numbers that exponent are integer given a base

ex: [ 1 4 16 27 64 100 1024 65536 531441 ] base = 4

    1 = 4^0
    4 = 4^1
    16 = 4^2
    1024 = 4^5
    65536 = 4^8

    output: 5 
    we have 5 that fit the criteria

"""

import math
from typing import List


def solution(numbers: List[int], base: int):

    count = 0

    for number in numbers:

        exponent = math.log(number, base)
        
        # compares the exponent with its rounded number using a precision
        # absolute tolerance lets me compare exponent and round(exponent) to see 
        # if the difference is less than or equal to 0.000000001
        if math.isclose(exponent, round(exponent), abs_tol=1e-9):
            exponent = round(exponent)

        print(number,exponent)
        print()

        if exponent % 1 == 0:
            count += 1

    print("----------------------")

    return count

print(solution([1, 4, 16, 27, 64, 100, 1024, 65536, 531441], 4))
print()

print(solution([100, 10, 1100, 1000000, 10100, 1000100, 1000], 10))
print()
