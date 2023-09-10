class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
                                        
        m,n=len(matrix),len(matrix[0])  # [[0,1,1,1],  # global array size 3 represents the number of lines m
                                        #  [1,1,1,1],  # length of single array inside represents the number of column n
                                        #  [0,1,1,1]]
        count=0 

        cumMatrix = [[0] * n for i in range(m)]   # matrix of n lines and m columns
                                                  # _ can be used instead of i means variable thats not gonna be used after

        # copy first column inside cumulative matrix
        for i in range(m):
            cumMatrix[i][0]=matrix[i][0]      # [0,1,0]
            count+=cumMatrix[i][0]            # when a spot is 1 it is equivalent to a matrix containing 1 of size 1x1

        # copy first row inside cumulative matrix
        for j in range(1,n):                  # range from 1 to lenght of array because we already counted the value of index 0 with column
            cumMatrix[0][j]=matrix[0][j]      # [1,1,1]
            count+=cumMatrix[0][j]           # when a spot is 1 it is equivalent to a matrix containing 1 of size 1x1

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    cumMatrix[i][j] = min(cumMatrix[i - 1][j], cumMatrix[i][j - 1], cumMatrix[i - 1][j - 1]) + 1
                    count += cumMatrix[i][j]
        return count


        

        
        

        
        