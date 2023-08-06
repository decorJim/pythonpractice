class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:  
                # if same element as left neighboor then duplicate
                continue
                
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    # too small move left pointer sorted small->big
                    # moving to right get a bigger number 
                    j+=1
                elif sum>0:
                    # too big move right pointer big->small
                    # moving to left get a smaller number
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1   # after adding an answer for current iteration move left pointer to next element
                           # code above is going to adjust the other pointers
                    while nums[j] == nums[j-1] and j<k:
                      j+=1      
        
        return ans
                
