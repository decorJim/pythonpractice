class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet=set()
        for i in range(len(nums)):
           numSet.add(nums[i])               # put all numbers in a set so there are no duplicate

        missings=[]                          # to store the missing numbers
        for i in range(1,len(nums)+1):       # from 1 to len+1
            if i not in numSet:              # if i is not in the set we know it is missing
              missings.append(i)             
        return missings