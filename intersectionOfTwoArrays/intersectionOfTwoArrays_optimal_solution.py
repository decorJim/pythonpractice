from typing import List

def intersectionsOfArray(nums1: List[int], nums2: List[int]):

    numbers = set()

    # O(n)
    for num in nums1:

        # we dont care about duplicates
        numbers.add(num)

    ans = []

    # O(n)
    for num in nums2:

        if num in numbers:

            # we dont want duplicates so when one is added remove num from set so a duplicate will not add it
            numbers.remove(num)
            ans.append(num)

    return ans

print(intersectionsOfArray([1,2,2,1], [2,2]))
print()

print(intersectionsOfArray([4,9,5], [9,4,9,8,4]))
print()
