class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp=set()                       # set to store unique numbers
        for i in range(len(nums)):
            if nums[i] not in tmp:      # if the number is not in the set 
                tmp.add(nums[i])        # add it to the set
            else:
                return True             # else there is a duplicate
        return False                    # if all number got added to the set then no duplicate