from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:

    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
    print()

    nbRows = len(matrix)
    nbColumns = len(matrix[0])

    cache = {} # (row, column) -> maxLength

    def helper(row, column):

        # if out of bounds end recursion
        if row >= nbRows or column >= nbColumns:
            return 0
        
        # if the key not in cache -> compute maxLength
        if (row, column) not in cache:
            down = helper(row + 1, column)
            right = helper(row, column + 1)
            diagonal = helper(row + 1, column + 1)

            # put random value for key value pair to set 
            # else if it tries to compute 1 + min(down,right,diagonal) one of the 3 
            # might be a nested call and not have a value yet which causes error 
            # when setting
            cache[ (row, column) ] = 0

            # check if the current value at that position is 1
            if matrix[row][column] == "1":
                
                # if all 3 position has value 1 then min is 1
                # if one or more is not then fails to meet 
                # condition of whole submatrix of 1 so min = 0
                cache[ (row, column) ] = 1 + min(down, right, diagonal)

        print("row", row, "column", column, "length", cache[ (row, column)])
        print()
        return cache[ (row, column) ]
    
    # matrix initial call
    helper(0,0)

    # area of a square is length ^ 2
    return pow(max(cache.values()),2)



matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))



