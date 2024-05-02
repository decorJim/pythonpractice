from typing import List

def temperature(tempratureArray:List[int]):

    rightSum = 0
    i = 0
    while i < len(tempratureArray):
        rightSum +=  tempratureArray[i]
        i += 1

    allMax = []

    leftSum = 0
    j = 0
    while j < len(tempratureArray):
        
        leftSum += tempratureArray[j]
        
        maxSum = max(leftSum,rightSum)
        allMax.append(maxSum)
        
        rightSum -= tempratureArray[j]
        
        j += 1

    return max(allMax)

    
"""
Find the maximum aggregate temperature changed evaluated among all the days.
ex - [-1,2,3] - 5
explanation -
[-1],[-1,2,3] - max(-1,4) = 4
[-1,2],[2,3] - max(1,5) = 5
[-1,2,3][3] - max(4,3) = 4
"""

print(temperature([-1,2,3]))








    








