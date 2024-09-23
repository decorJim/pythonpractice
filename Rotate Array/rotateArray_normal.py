

from typing import List


def rotateArray(nums: List[int], k:int):

    # O(n^2) time complexity
    
    counter = 0
    while counter < k:
        i = 0
        j = len(nums) - 1

        while i < len(nums):

            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        counter += 1

    return nums

#  i           j
# [1,2,3,4,5,6,7]
#    i         j 
# [7,2,3,4,5,6,1]
#      i       j
# [7,1,3,4,5,6,2]
#        i     j
# [7,1,2,4,5,6,3]
#          i   j
# [7,1,2,3,5,6,4]
#            i j
# [7,1,2,3,4,6,5]
#              ij
# [7,1,2,3,4,5,6]

print(rotateArray([1,2,3,4,5,6,7], 3))

