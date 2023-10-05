from typing import List


class Solution:
    def twoSum(self,nums:List[int], target:int)->List[int]:
        if len(nums)==0:
          return

        complement={}    # always store a number when his complement => number+complement=target

        for i in range(len(nums)): 
          
          if (target-nums[i]) in complement:        # complement=target-number
            return [i,complement[target-nums[i]]]   # if its in map then WE KNOW NUMBER+COMPLEMENT=TARGET 
                                                    # return our 2 index
          
          complement[nums[i]]=i                     # if number's complement is not there
                                                    # store it, it might be the complement of the next number
        