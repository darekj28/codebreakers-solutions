class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # check if input is empty
        if len(grid) == 0:
            return -1
        numRows = len(grid)
        numCols = len(grid[0])
        
        # return -1 if the starting or ending cell is blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        # bfs through the grid
        seen = set()
        queue = collections.deque()
        queue.append([0, 0, 1]) # row, column, distance
        seen.add((0, 0))
        while queue:
            currRow, currCol, currDist = queue.pop()
            
            # check if we reached our destination
            if currRow == numRows - 1 and currCol == numCols - 1:
                return currDist
            
            # check our neighbors
            for dir in [[-1,-1],[1,1],[1,0],[-1,0],[0,1],[0,-1],[1,-1],[-1,1]]:
                newRow = currRow + dir[0]
                newCol = currCol + dir[1]
                # if we're not out of bounds and haven't seen the cell yet, add it to our queue
                if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] == 0 and (newRow, newCol) not in seen:
                    queue.appendleft((newRow, newCol, currDist + 1))
                    seen.add((newRow, newCol))
        # if we finish our bfs and never reach the endpoint, it's impossible to get there
        return -1