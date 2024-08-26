from typing import List


def missingNumber(nums: List[int]):

    # the sum we expect if all numbers were present
    wantedSum = sum(num for num in range(len(nums) + 1))
    # the sum of the numbers we actually have
    actualSum = sum(nums)

    # the difference gives us what was suppose to be there
    return wantedSum - actualSum

print(missingNumber([3,0,1]))