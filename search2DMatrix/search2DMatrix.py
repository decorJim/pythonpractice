from typing import List


def search2DMatrix(matrix: List[List[int]], target: int):

    # time complexity O(logm) + O(logn)

    nbRows = len(matrix)
    nbColumns = len(matrix[0])

    # binary search for vertical
    top = 0
    bottom = nbRows - 1

    # this binary search only looks the row
    # where target is between its first element and last element
    while top <= bottom:

        middleRow = (top + bottom) // 2

        # check if the target is bigger than the middle row's last element 
        if target > matrix[middleRow][-1]:
            # probably in a lower row with bigger elements
            top = middleRow + 1

        # check if the target is less than the middle row's first element
        elif target < matrix[middleRow][0]:
            # probably in a higher with lower elements
            bottom = middleRow - 1

        else:
            break


    # if no target value exist in the matrix return false
    if not (top <= bottom):
        return False
    
    # row where target is in
    middleRow = (top + bottom) // 2
    
    left = 0
    right = nbColumns - 1

    while left <= right:

        middle = (left + right) // 2

        if target > matrix[middleRow][middle]:
            
            left = middle + 1

        elif target < matrix[middleRow][middle]:

            right = middle - 1

        else:
            return True
        
    return False

print(search2DMatrix([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3))
print()

print(search2DMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print()
