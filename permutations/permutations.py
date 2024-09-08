from typing import List


def permute(nums: List[int]):
    print(nums)
    print()

    ans = []

    # is there is one item in the list return that
    if len(nums) == 1:
        return [ nums.copy() ]
    
    for i in range(len(nums)):

        # pop first element in the array
        n = nums.pop(0)

        permutations = permute(nums)

        print("permutations",permutations)
        for perm in permutations:

            perm.append(n)

        print("append", permutations)

        # function that adds all elements from permutations into ans
        ans.extend(permutations)
    
        # for next iteration we want to restore so it pops the right element
        # ex: [2,3] -> n = 2, nums = [3]
        # if we dont add back to nums then next iteration we pop 3 and nums = []
        # so size shrinks and either length is below 0
        # or permutation not enough elements
        nums.append(n)

    return ans


print(permute([1,2,3,4]))
print()

