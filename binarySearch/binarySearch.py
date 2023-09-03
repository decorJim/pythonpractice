class Solution:
    def compute(self,i:int,j:int,target:int,nums:List[int]):
        mid=i+floor((j-i)/2)      # find the middle index have to round down in python
                                  # i+ because if index given is 3 to 5 we get 1 so 3+1=4 is the middle
        if nums[i]==target:       # checks if one of the pointers is the element
            return i
        if nums[mid]==target:
            return mid
        if nums[j]==target:
            return j
        
        if nums[i]<target<nums[mid]:                   # if we know the target is between i and mid
            return self.compute(i,mid,target,nums)     # calls the same function but only check for i and mid
        if nums[mid]<target<nums[j]:                   # if we know the target is between mid and j
            return self.compute(mid+1,j,target,nums)   # calls the same function but only check for mid+1 and j
        else:
            return -1                                  # cannot find it in either return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.compute(0,len(nums)-1,target,nums) # first call the function for the whole array
                                                       # 0 to lenghtArray-1