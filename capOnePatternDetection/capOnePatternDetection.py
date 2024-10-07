"""
given an array and a pattern, we want to know how many subsets of the
array matches the pattern

"""

from typing import List


def evaluatePattern(previous, current):

    if current > previous:
        return 1
    
    elif current < previous:
        return -1
    
    else:
        return 0


def solution(array: List[int], pattern: List[int]):

    i = 1
    nbSubarray = 0

    while i < len(array):

        counter = 0

        j = i
        while j < len(array) and counter < len(pattern):

            wantedPattern = pattern[counter]
            currentPattern = evaluatePattern(array[j - 1], array[j])

            if currentPattern == wantedPattern:
                counter += 1

                if counter == len(pattern):
                    print(array[i:j+1])
                    nbSubarray += 1
                    break
                
                j += 1

            else:
                counter = 0
                break

        i += 1

    return nbSubarray



# 4,4,1  5,5,3
print(solution([2, 4, 4, 1, 5, 5, 3, 2, 2, 6], [1,0,-1]))
print()

print(solution([1, 2, 2, 3, 4, 4, 5, 6, 7, 6, 5, 5, 4, 4, 3, 2], [1, 0, 1, -1]))
print()

print(solution([8, 5, 6, 6, 4, 3, 4, 4, 7, 7, 2, 2], [-1,1,0]))
print()

print(solution([3, 2, 4, 4, 5], [-1, 1, 0]))
print()

print(solution([7, 5, 8, 8, 6, 9, 9, 7, 6, 10], [-1, 1, 0, -1]))
print()