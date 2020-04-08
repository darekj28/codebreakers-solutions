class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # ensure the input isn't empty
        if len(grid) == 0:
            return 0
        numRows = len(grid)
        numCols = len(grid[0])
        
        # get set of fresh oranges
        freshOranges = set()
        # get queue of rotten oranges for bfs
        rottenOranges = collections.deque()
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    freshOranges.add((r,c))
                if grid[r][c] == 2:
                    rottenOranges.append((r,c,1)) # (row, column, timeElapsed)
        
        timeElapsed = 0
        if len(freshOranges) == 0:
            # if no fresh oranges exist
            return timeElapsed
        if len(rottenOranges) == 0:
            # if the fresh oranges will never rot
            return -1
        
        # bfs through the grid from where the rotten oranges are
        while rottenOranges:
            currRow, currCol, timeElapsed = rottenOranges.pop()
            for dir in [[-1,0],[1,0],[0,1],[0,-1]]:
                newRow = currRow + dir[0]
                newCol = currCol + dir[1]
                # if a rotten orange is adjacent to a fresh one
                if (newRow, newCol) in freshOranges:
                    # remove the freshorange from the list of fresh oranges
                    freshOranges.remove((newRow,newCol))
                    # add the newly rotten oranges to our queue of rotten oranges
                    rottenOranges.appendleft((newRow, newCol, timeElapsed + 1))
                if len(freshOranges) == 0:
                    # all fresh oranges have rotten
                    return timeElapsed
        # some fresh oranges cannot be reached and will never rotten
        return -1
                    
            