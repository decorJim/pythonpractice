"""
The cost of a stock on each day is given in an array arr. An investor
wants to buy the stocks in triplets such that the sum of the cost for 
3 days is divisible by d

The goal is to find the number of distinct triplet (i, j, k) such
that i < j < k and the sum arr[i] + arr[j] + arr[k] is divisible by d

ex: arr = [ 3 3 4 7 8 ] and d = 5

Triplet with indices (0, 1, 2) sum = 3 + 3 + 4 = 10
Triplet with indices (0, 2, 4) sum = 3 + 4 + 8 = 15
Triplet with indices (1, 2, 4) sum = 3 + 4 + 8 = 15

answer = 3
"""

from typing import List


def getTripletCount(arr: List[int], d:int):

    ans = 0

    print(arr)

    # (arr[i] + arr[j] + arr[k]) % d = 0
    # we have 2 pointers i and j
    # so arr[i]%d + arr[j]%d + arr[k]%d = 0
    # arr[k]%d = -arr[i]%d - arr[j]%d
    # arr[k]%d = -(arr[i] + arr[j])%d
    # so we are storing any possible arr[k]%d
    complements = {}

    for i in range(len(arr)):

        j = i + 1

        while j < len(arr):

            currentSum = arr[i] + arr[j]

            # arr[k]%d
            complement = (-currentSum) % d

            if complement in complements:
                # there is x way to form triplet
                # example currentSum = 3 + 2 = 5 and k = 2
                # -5 % 2 = 1 => 2*-3 + 1 so remainder is 1
                # if we already stored 7%2 = 1 and 15%2 = 1
                # we can form 2 triplet [ 3 2 7 ] and [ 3 2 15 ]
                # so we add to count
                ans += complements[complement]

            j += 1

        # current arr[i]%d might be a complement for
        # another duplet
        currentComplement = arr[i] % d

        if currentComplement in complements:
            complements[currentComplement] += 1

        else:
            complements[currentComplement] = 1

    return ans


print(getTripletCount([3,3,4,7,8], 5))
print()

print(getTripletCount([3,3,3,4,8], 5))
print()

