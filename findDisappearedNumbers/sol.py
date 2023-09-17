class Solution:
    def findDisappearedNumbers(self,nums: List[int])-> List[int]:
        # mark present value by converting element into negative at index value+1
        for n in nums:
            i=abs(n)-1
            nums[i]=-1*abs(nums[i])

        res=[]
        for i,n in enumerate(nums):   # iterate through index and value at same time
            if n>0:
                res.append(i+1)
        return res
            
