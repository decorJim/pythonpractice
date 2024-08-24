from typing import List

def mergedSortedArray(nums1: List[int], m:int, nums2:List[int], n:int):

    # last index in nums1
    lastIndex = m + n - 1

    i = m - 1
    j = n - 1

    # normally in loop range(3) -> 0 1 2 stop
    # reverse is 2 1 0 stop
    while i >= 0 and j >= 0:

        # all index are the real size - 1
        if nums1[i] > nums2[j]:

            nums1[lastIndex] = nums1[i]
            i -= 1

        else:

            nums1[lastIndex] = nums2[j]
            j -= 1

        lastIndex -= 1

    # put remaining elements of nums2 in nums1
    while j >= 0:

        nums1[lastIndex] = nums2[j]
        j -= 1
        lastIndex -= 1

    return nums1


print(mergedSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3))
print()

print(mergedSortedArray([1], 1, [], 0))
print()



    

        