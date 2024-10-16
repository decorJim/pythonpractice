"""
[
    [1, 8, 4, 3, 4],
    [2, 8, 0, 3, 1],
    [0, 7, 9, 0, 8],
    [5, 0, 3, 1, 6],
    [1, 5, 0, 3, 1]
]

you are given a square matrix of integer
matrix of size n x n. Let's define a bouncing 
diagonal as a sequence which starts from
a cell of the leftmost column and continues 
diagonally ( up-right ) until it reaches 
the rightmost column bouncing vertically if 
it reaches the top of the matrix.

sums up each item in the diagonal path
then return the array of all the path sum 
in ascending order
"""

from typing import List


def solution(matrix: List[List[int]]):

    nbRows = len(matrix)
    nbColumns = len(matrix[0])

    pathSums = []


    # for each row of the first column we have to find an
    # element in each column so time complexity is O(n^2)

    # go through all the rows
    for i in range(nbRows):

        start = matrix[i][0]
        print("start",start)
        print()

        currentSum = start

        row = i
        column = 0

        direction = -1

        # go through all the columns
        while row + direction < nbRows and column + 1 < nbColumns:

            # check if the top right position is within bounds 
            if row + direction >= 0:
                row += direction

            # change direction else
            else:
                direction *= -1
                row += direction

            # always checking for the neighboor column
            column += 1

            print(matrix[row][column])
            print()

            currentSum += matrix[row][column]
            
        pathSums.append(currentSum)
    
    pathSums.sort(reverse = True)
    return pathSums



matrix = [
    [1, 8, 4, 3, 4],
    [2, 8, 0, 3, 1],
    [0, 7, 9, 0, 8],
    [5, 0, 3, 1, 6],
    [1, 5, 0, 3, 1]
]

print(solution(matrix))
print()

