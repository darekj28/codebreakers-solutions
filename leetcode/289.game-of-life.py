"""
Motivation:
The problem is relatively straightforward. We loop through the matrix and count all of the current
cell's neighbors. Then we store its number of neighbors in an auxillary matrix. We provide a 
solution in linear space because we assume that the contents of the cells should be 0,1 bits as 
opposed to integers. If one wanted to update the matrix without an auxillary matrix, they would 
have to replace the current cell of the board with a code that represents both the previous state
and next state of the board (so that the current cell's neighbors would be able to count their 
own neighbors properly). To do this, it would require linear space since integers require multiple 
bits. Note that if the board were infinite, we would be required to solve the problem in blocks,
potentially row by row. One could also take advantage of sparseness, and only store the location of
live cells in the matrix if only a few are alive relative to the size of the board.

Time Complexity:
The time complexity is linear to the size of the matrix since we loop through a constant number of
times. We visit each cell in the board a constant number of times: once when calculating the number 
of neighbors it has, up to 8 times for counting a neighboring cell's number of neighbors, and once 
again to update all the values in the matrix. 

Space Complexity:
The space complexity is linear to the input since our neighbors matrix is the same size.
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRows = len(board)
        # check if board is empty
        if numRows == 0:
            return
        numCols = len(board[0])
        
        # direction array for visiting neighbors of current cell
        dirs = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        
        # matrix to keep track of number of neighbors for cell at board[r][c]
        neighsMatrix = [[0 for i in range(numCols)] for j in range(numRows)]
        for r in range(numRows):
            for c in range(numCols):
                numNeighs = 0
                for dir in dirs:
                    newR = r + dir[0]
                    newC = c + dir[1]
                    # continue to next  neighbor if newR, newC are out of bounds
                    if newR < 0 or newC < 0 or newR == numRows or newC == numCols:
                        continue
                    numNeighs += board[newR][newC]
                neighsMatrix[r][c] = numNeighs
        
        # update original matrix with the new values
        for r in range(numRows):
            for c in range(numCols):
                numNeighs = neighsMatrix[r][c]
                # a new cell should be born
                if board[r][c] == 0 and numNeighs == 3:
                    board[r][c] = 1
                # a pre-existing cell should die from under or over population
                elif board[r][c] == 1 and (numNeighs < 2 or numNeighs > 3):
                    board[r][c] = 0
                    