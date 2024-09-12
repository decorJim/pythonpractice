


from typing import List


def findDuplicate(nums: List[int]):

    # both starts at the same index 0
    slow = 0
    fast = 0

    while True:

        slow = nums[slow]

        # we are traveling twice faster than slow
        # we first extract the value at nums[fast] which is another index
        # we then set fast as the value of this other index
        fast = nums[nums[fast]]


        # when they meet again break out of the loop
        if slow == fast:
            break

    # our second slow pointer create at index 0
    slow_2 = 0

    while True:

        slow = nums[slow]

        slow_2 = nums[slow_2]

        # the intersection will be the first element entering a cycle where the duplicate will always be at
        # if we map out index to value then a duplicate will create a cycle in the imaginary linked list
        if slow == slow_2:
            break

    return slow
    
print(findDuplicate([1,3,4,2,2]))
print()

print(findDuplicate([3,1,3,4,2]))
print()

print(findDuplicate([3,3,3,3,3]))
print()




