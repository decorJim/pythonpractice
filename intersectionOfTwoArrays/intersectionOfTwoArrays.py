from typing import List


def intersection(nums1:List[int],nums2:List[int]):
    uniques=set()

    for i in nums1:
        uniques.add(i)

    res=set()
    for i in nums2:
        if i in uniques:
            res.add(i)
    
    return sorted(res)



nums1=[2,3,4,2,54,6,4]
nums2=[1,3,2,3,5,4,5]

print(intersection(nums1,nums2))

nums1=[-1,-2,0,6,4,2,-6]
nums2=[-3,-6,2,4]

print(intersection(nums1,nums2))

nums1=[]
nums2=[2,1,4,2,3]

print(intersection(nums1,nums2))