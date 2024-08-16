from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
        
        nbRows = len(matrix)
        nbColumns = len(matrix[0])

        # build a matrix of same size to keep track of maxLength of square with 0
        cumulativeMatrix = []

        for _ in range(nbRows):
            
            row = []
            for _ in range(nbColumns):
                row.append(0)

            cumulativeMatrix.append(row)

        # copy first column to cumulative matrix since they are the only ones possible with maximum square with length 1
        # compare max to see if there is any 1 to set the maximum to 1
        maxLength = 0
        for i in range(nbRows):
            print(i)
            cumulativeMatrix[i][0] = int(matrix[i][0])
            maxLength = max(maxLength, cumulativeMatrix[i][0])

        # same with the first row check if there is any one
        # set maximum
        for j in range(nbColumns):
            cumulativeMatrix[0][j] = int(matrix[0][j])
            maxLength = max(maxLength, cumulativeMatrix[0][j])

        # for other positions, check top, left, top diagonal to see if every one is a 1 then minimum is 1 and +1 for its own 1 
        # if 4 positions are 1 then it is a square of length 2
        for row in range(1,nbRows):
            for column in range(1, nbColumns):
                if matrix[row][column] == "1":
                    cumulativeMatrix[row][column] = 1 + min(cumulativeMatrix[row - 1][column], cumulativeMatrix[row][column - 1], cumulativeMatrix[row - 1][column - 1])
                    maxLength = max(maxLength, cumulativeMatrix[row][column])

        return pow(maxLength, 2)