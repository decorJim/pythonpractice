from typing import List


def subarraySumEqualsK(nums:List[int], k:int):

    # keeps track of the subarray's sum and its count
    # [ 1 -1 1 1 1 ] if k = 2 we know that we can remove either
    # nothing (1-1+1+1+1) = 2 or the prefix [ 1 -1 1 ] so that (1+1) = 2
    # [ 1 -1 1 ] -> { (1-1+1):1 }
    # 0:1 is the empty prefix we remove nothing
    prefixCount = { 0:1 }

    # number of 
    numberOfSubarraysK = 0

    currentSum = 0

    for num in nums:

        currentSum += num

        # currentSum = [ 1 -1 1 1 1 ] -> k = [ 1 1 ] at the end
        # prefixToRemove = [ 1 -1 1 ]
        # we are checking if the prefix to remove from the current
        # subarray exists ?
        prefixToRemove = currentSum - k

        if prefixToRemove in prefixCount:
            # if there is 2 ways that the current subarray can sum up to k
            # then add 2 -> numberOfSubarraysK += 2
            # currentSum - k = 3 - 2 = 1
            # [1 -1 1 1 1] k = 2     prefixCount = { 0:1, }
            # prefix = [] k = [1 -1 1 1 1]   
            # prefix = [ 1 -1 1 ] k = [1 1]
            numberOfSubarraysK += prefixCount[ prefixToRemove ]

        # the point of this if else is to mark every
        # current subarray's sum as a possible prefix to remove
        # for futur iterations
        # the subarray itself is another prefix for bigger subarrays
        if currentSum in prefixCount:

            prefixCount[ currentSum ] = prefixCount[ currentSum ] + 1

        else:

            prefixCount[ currentSum ] = 1

    return numberOfSubarraysK


print(subarraySumEqualsK([1,1,1], 2))
print()

print(subarraySumEqualsK([1,2,3], 3))
print()

print(subarraySumEqualsK([1,2,1,2,1], 3))
print()
