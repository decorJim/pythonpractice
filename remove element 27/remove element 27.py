from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         newindex=0
         if 0<=len(nums)<=100 and 0<=val<=100:
           i=0
           while i in range(len(nums)):
              print("i:",i,"element:",nums[i])
              print("newIndex:",newindex,"element:",nums[newindex])
              print("--------------------------------------------")
              if nums[i]!=val:
                 nums[newindex]=nums[i] # overwrite at newIndex even if it is the same value
                 newindex+=1 # always first advance newIndex to set next spot to overwrite 
              i+=1
           print("nums",nums)
           return newindex
         
nums=[9,48,28,34,8,3,5,2,4,3,7,2]
print(Solution().removeElement(nums,3))

# nums[newindex]=nums[i] is useful because even if we do pointless action such as overwriting with the same element
# the useful part is once we i detects the target newIndex is kept at the target to mark it
# then when i advance until it finds an element to replace the target by
# it is useful because while both i and newIndex are advancing nums[newindex]=nums[i] is performed 
# no nested loops