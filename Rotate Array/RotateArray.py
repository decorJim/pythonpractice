class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)  # if the length of the array is the same as k
                       # we are basically doing nothing    ex: k=4 and len(nums)=4  4%4=0
        
        i,j=0,len(nums)-1  # pointers at start and end of array

        while i<j:   # reverse array 
            nums[i],nums[j]=nums[j],nums[i]
            i,j=i+1,j-1

        i,j=0,k-1    # if k is 2 then the first 2 elements must be rotate 
                     # aka index 0 and index 1 k-1 is the right index
        while i<j:   # reverse first k elements
            nums[i],nums[j]=nums[j],nums[i]
            i,j=i+1,j-1

        i,j=k,len(nums)-1

        while i<j:
            nums[i],nums[j]=nums[j],nums[j]
            i,j=i+1,j-1
        
        
        
        