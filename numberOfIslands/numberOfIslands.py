from typing import List
from collections import deque

def numIslands(grid: List[List[str]]) -> int:

    if not grid:
        return 0
    
    nbRows = len(grid)
    nbColumns = len(grid[0])

    visited = set()

    nbIslands = 0

    def bfs(row, column):
        
        # keep tracks of what to visit next
        queue = deque()

        # mark current position as visited
        visited.add((row, column))
        queue.append((row, column))

        while queue:

            row, column = queue.popleft()

            # check adjacent position of what we just pop
            #                up     down     left    right
            directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

            # computes all possible next position to visit
            for directionRow, directionColumn in directions:

                newRow = row + directionRow
                newColumn = column + directionColumn

                # makes sure new position is now outside of grid 
                if ( (0 <= newRow < nbRows) and (0 <= newColumn < nbColumns) and 
                (grid[newRow][newColumn] == "1") and ((newRow, newColumn) not in visited) ):

                    # add new position to queue so that algorithm keeps running
                    queue.append((row + directionRow, column + directionColumn))
                    visited.add((row + directionRow, column + directionColumn))


    # double loop checks all positions in grid
    for row in range(nbRows):

        for column in range(nbColumns):

            if grid[row][column] == "1" and (row, column) not in visited:

                # detect all positions that belong to the same island and mark them
                bfs(row, column)
                # increase the count of island
                nbIslands += 1

    return nbIslands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))
print()

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))
print()