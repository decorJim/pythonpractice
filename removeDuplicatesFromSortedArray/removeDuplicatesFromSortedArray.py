from typing import List


def removeDuplicatesFromSortedArray(nums: List[int]):

    # not duplicates so return 1 for unique element
    if len(nums) == 1:
        return 1

    # pointer that will stay on spots with duplicates values
    marker = 0

    for i in range(len(nums)):

        # if its the first spot or the number is equal
        # to its left neighboor copy its value to
        # the spot of the marker then change the marker spot
        if i == 0 or nums[i] != nums[i - 1]:

            # the marker always ends up last spot at 
            # 1 spot after the last 
            nums[marker] = nums[i]
            marker += 1

    # edge case where there is a duplicate but len is 2
    # [ 1 1 ] we need to return 1 because by removing the duplicate
    # [ 1 ] we have 1 element 
    if marker == 0:
        return 1
    
    return nums


print(removeDuplicatesFromSortedArray([1,1,2]))
print()

print(removeDuplicatesFromSortedArray([0,0,1,1,1,2,2,3,3,4]))
print()




