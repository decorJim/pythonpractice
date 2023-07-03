class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         """ 
             new index to override previous values in nums
             cuz final answer is checked using original nums
         """
         newindex=0
         if 0<=len(nums)<=100 and 0<=val<=100:
           i=0
           while i in range(len(nums)):
              print(nums[i],nums[i]==val)
              if nums[i]!=val:
                 nums[newindex]=nums[i]
                 """ switch newindex to next spot to overwrite """
                 newindex+=1  
              i+=1
           print("nums",nums)
           return newindex