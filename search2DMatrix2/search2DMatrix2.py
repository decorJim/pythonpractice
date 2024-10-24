from typing import List


def search2DMatrix2(matrix: List[List[int]], target: int):

    nbRows = len(matrix)
    nbColumns = len(matrix[0])

    # starting point at top right corner of matrix
    # why ? because by tracing out the sort directions
    # we want a starting point where we have a direction with lower numbers increasing toward the point
    # and a direction with increasing outward from the point
    # only 2 possible options top right corner or lower left corner
    # the other 2 edges have 2 outward or inward directions so no good
    
    row = 0
    column = nbColumns - 1

    while 0 <= row < nbRows and 0 <= column < nbColumns:

        if matrix[row][column] < target:
            row += 1

        elif matrix[row][column] > target:
            column -= 1

        elif matrix[row][column] == target:
            return True
        
    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(search2DMatrix2(matrix, 5))
print()

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(search2DMatrix2(matrix, 20))
print()