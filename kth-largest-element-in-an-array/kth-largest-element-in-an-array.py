#
# In this problem we dont care about duplicates meaning if I want the 3rd largest there is duplicate of 5 but the answer is still 5
#

import heapq
from typing import List


def kThLargestElementInArray(nums:List[int], k:int):
    print()
    print(nums)
    print()
    heapq._heapify_max(nums)
    print(nums)
    print()

    kLargest = 0
    for _ in range(k):
        kLargest = heapq._heappop_max(nums)
        print("pop",kLargest)
    
    print()

    return kLargest


print(kThLargestElementInArray([3,2,3,1,2,4,5,5,6],4))
