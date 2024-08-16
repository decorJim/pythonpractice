from typing import List


def maximumSubarray(nums:List[int]):

    maxSum = float("-inf")

    currentSum = 0

    for i in range(len(nums)):

        # this only makes sure that if the previous iteration's number is negative and 
        # dropped the current sum below 0 then the whole window is no good start window 
        # with current element
        # this also allows an array full of negative then the subarray is pof size 1
        # containing the negative closest to 0
        # this way the the current sum is always the current negative
        # we compare it with the largest negative
        if currentSum < 0:
            currentSum = 0

        # add current number in sum
        currentSum += nums[i]

        maxSum = max(currentSum, maxSum)

    return maxSum


print(maximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))
print()

print(maximumSubarray([1]))
print()

print(maximumSubarray([5,4,-1,7,8]))
print()
