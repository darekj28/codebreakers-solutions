class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # make sure grid isn't empty
        if len(grid) == 0:
            return 0
        # set to keep track of cells we've visited
        visited = set()
        # direction array for visiting neighbors of current cell. 
        # each element in the dirs arr represent [deltaY, deltaX] for each adjacent cell in the
        # grid. For example, [-1,0] represents the cell above the current cell, while [1,1] 
        # would represent the change in the rowNum and colNum for the cell to the bottom right of
        # the current cell
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # we get the size of the current island and set it to maxArea if it is greater
                maxArea = max(maxArea, self._getIslandSize(visited, grid, dirs, r, c))
        return maxArea
    
    # helper function which will DFS through the current island
    def _getIslandSize(self, visited, grid, dirs, r, c):
        # base case
        if (r,c) in visited or grid[r][c] == 0:
            return 0
        # update our visited set
        visited.add((r,c))
        
        additionalArea = 0
        for dir in dirs:
            # get potential new indices for our neighboring cells
            newR = r + dir[0]
            newC = c + dir[1]
            # filter out the potential indices that are out of bounds
            if newR < 0 or newC < 0 or newR == len(grid) or newC == len(grid[0]):
                continue
            # sum the area of the neighboring land
            additionalArea += self._getIslandSize(visited, grid, dirs, newR, newC)
        # return +1 to account for current cell's land
        return additionalArea + 1
                