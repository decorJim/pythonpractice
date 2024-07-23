import heapq
from typing import List

# overall time complexity O( nlogn + (k-1)logn ) worst case k = n then O( nlogn )
def kThSmallestInSortedArray(matrix:List[List[int]], k:int):

    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print()

    pq = []

    # O(nlogn) where there is n columns and each insertion takes O(logn)
    for j in range(len(matrix[0])):
        
        # put first row of matrix in min priority queue
        heapq.heappush(pq, (matrix[0][j], 0, j) )

    print(pq)
    print()

    # after k-1 iteration I want the kth smallest to be in the priority queue
    # k-1 operations of extraction O((k-1)logn)
    # k-1 operations of insertion we consider worst case O((k-1)logn)
    # O( (k-1)logn + (k-1)logn ) -> O((k-1)logn)
    while k > 1:

        num, i, j = heapq.heappop(pq)
        print(pq)
        print("smallest",num)

        # compare the next element in the column with the others
        # move current num's row index -> i+1 to next and push it
        # column doesnt change -> j
        if i+1 < len(matrix):
            heapq.heappush(pq, (matrix[i+1][j], i+1, j))
        print(pq)
        print()

        k -= 1

    # kth smallest at index 0 of queue
    print(pq)
    print()

    # extract the element at index 0 (num, row, column) -> we extract the num so index 0
    return pq[0][0]


matrix = [[1,5,9],[10,11,13],[12,13,15],[20,23,25]]
k = 4

print(kThSmallestInSortedArray(matrix,k))

print()

matrix = [[1,18,25],[2,19,26],[3,25,32]]
k = 6

print(kThSmallestInSortedArray(matrix,k))

