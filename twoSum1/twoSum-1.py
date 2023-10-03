from typing import List


def two_sum(nums:List[int], target:int)->List[int]:
    if len(nums)==0:
        return
    
    complement={}
    for i in range(len(nums)):
        if (target-nums[i]) in complement:
           return [i,complement[target-nums[i]]]
        complement[nums[i]]=i



nums=[2,3,6,3,6]
target=5

print(two_sum(nums,target))

nums=[]
target=5

print(two_sum(nums,target))

nums=[-3,-2,0,3,4,6,5,-8]
target=-5

print(two_sum(nums,target))

nums=[2,5,3,2,1,4,12]
target=6

print(two_sum(nums,target))
