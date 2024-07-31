from typing import List


def bestTimeToBuyAndSellStock(nums:List[int]):

    i = 0
    j = 1

    maxDifference = 0

    while j < len(nums):

        if nums[j] - nums[i] > maxDifference:
            maxDifference = nums[j] - nums[i]

        if nums[i] > nums[j]:
            i += 1

        else:
            j += 1

    return maxDifference



print(bestTimeToBuyAndSellStock([5,2,3,7,4,10,2]))