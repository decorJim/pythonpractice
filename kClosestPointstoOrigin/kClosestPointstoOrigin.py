import heapq
from math import sqrt
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    print(points)

    distances = []

    for subarray in points:
        distance = sqrt(pow(subarray[0] - 0,2) + pow(subarray[1] - 0,2))
        distances.append([distance,subarray[0],subarray[1]])

    print(distances)

    heapq.heapify(distances)

    print(distances)

    ans = []
    for _ in range(k):
        distance, x, y = heapq.heappop(distances)
        ans.append([x,y])

    return ans
        

points = [[1,3],[-2,2]]
k = 1

print()
print(kClosest(points,k))
print()





        