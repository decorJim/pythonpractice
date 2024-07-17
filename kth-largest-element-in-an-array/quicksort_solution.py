from typing import List


def kThLargestElementInArray(nums:List[int], k:int):

    # if k = 2 then I want the second largest in array -> if the array is sorted then the index will be this 
    # [ 100 300 900 20000 345000 ] in this array k = 2 then I want index 3 -> 5-2 = 3
    k = len(nums) - k

    def quickSelect(left, right):

        # pointer that marks elements larger than pivot to be switch
        j = left

        # pointer that finds elements smaller or equal to pivot to switch with j
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        print(nums[left:right + 1])
        # last switch of pivot with the first element found bigger than pivot in array
        nums[j], nums[right] = nums[right], nums[j]
       
        print(nums[left:right + 1])

        print("j",j)
        print("k",k)
        print()

        if j > k: # there are j elements bigger than current pivot -> rerun with smaller range 
            return quickSelect(left, j - 1)

        elif j < k:
            return quickSelect(j + 1, right)

        # when the pivot is equal to k -> we have k elements bigger than him so pivot is our answer
        else:
            return nums[j]

    return quickSelect(0, len(nums) - 1)


print(kThLargestElementInArray([3,2,1,5,6,4],2))
# [3,2,3,1,2,4,5,5,6]
print(kThLargestElementInArray([3,2,3,1,2,4,5,5,6],4))


