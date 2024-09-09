"""
An array of size n represents a set of available resources. Identify a subarray 
that optimally utilises these resources under the following constraints
- The subarray must have a specific length k
- all elements in the subarray must be unique representing distinct resource allocations
The ultimate goal is to find the subarray that maximizes the sum of the allocated resources
Return the sum for that subarray. If it is not possible to allocate resources per the contraints
return -1 

ex: 
n = 5
k = 3
arr = [1,2,3,7,3,5]
following subarrays:
[1,2,3] sum = 6
[2,3,7] sum = 12
[7,3,5] sum = 15
"""

from typing import List

def findOptimalResources(arr:List[int], k:int):

    if k > len(arr):
        return -1

    i = 0
    j = 0

    currentSum = 0
    maxSum = -1
    uniques = set()

    while j < len(arr):

        while i < j and (arr[j] in uniques or j - i + 1 > k):

            uniques.remove(arr[i])
            currentSum -= arr[i]

            i += 1

        currentSum += arr[j]
        uniques.add(arr[j])

        if j - i + 1 == k:
            maxSum = max(maxSum, currentSum)

        j += 1

    return maxSum

print(findOptimalResources([1,2,3,7,3,5], 3))
print()

print(findOptimalResources([1, 1, 1, 1], 3))
print()



