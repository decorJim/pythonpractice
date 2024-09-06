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

        # function to append many values to an array
        ans.extend(permutations)

        # put back element we popped at the back
        nums.append(n)

    return ans


permute([1,2,3])
print()

