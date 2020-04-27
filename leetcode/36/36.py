class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # instantiate sets to for each row, column, and box
        rowToSets = [set() for i in range(9)]
        colToSets = [set() for i in range(9)]
        boxToSets = [set() for i in range(9)]
        
        # for each cell, we want to add it to its corresponding row, col and box
        # if it already exists in any one of these sets, then the sudoku board is invalid
        for r in range(len(board)):
            for c in range(len(board[0])):
                # only check if the current cell isn't empty
                if board[r][c] != ".":
                    currNum = board[r][c]
                    # if the current cell's value is already stored, then we've broken the rules of a valid sudoku
                    if currNum in rowToSets[r] or currNum in colToSets[c] or currNum in boxToSets[self._coordToBoxNum(r,c)]:
                        return False
                    # mark all appropriate sets that the currNum has been seen
                    rowToSets[r].add(currNum)
                    colToSets[c].add(currNum)
                    boxToSets[self._coordToBoxNum(r,c)].add(currNum)
        return True
    
    # map r, c coordinates to box numbers 
    def _coordToBoxNum(self, r, c):
        return r//3*3+c//3