class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums.sort()
        
        ans=[]
       
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if(sum==0):
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1   # move j to right
                    k-=1   # move k to left
                    while j<k and nums[j]==nums[j-1]:    # skip if index gives same element as previous position (no duplicate triplet)
                        j+=1
                    while j<k and nums[k]==nums[k+1]:    # skip if index gives same element as previous position
                        k-=1
                        
                elif(sum<0):      # this condition can be reversed with the else the main point is to move different index
                    j+=1          # when the sum is either higher or lower than 0
                else:
                    k-=1
                
        return ans