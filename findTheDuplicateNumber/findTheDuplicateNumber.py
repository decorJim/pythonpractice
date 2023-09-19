class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet=set()         # since we are not allowed to modify original number set cannot contain duplicate
        for i in nums:       
            if i in numSet:  # when we encounter a number already in hash set
                return i     # return it as the duplicate
            numSet.add(i)    # else we just add it in the hash set