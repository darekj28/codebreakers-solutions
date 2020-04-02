class Solution(object):
    def spiralOrder(self, matrix):
        # initialize solution
        sol = []
        # check for an empty input
        if len(matrix) == 0:
            return sol
        # initialize bounds for perimeter to traverse
        minRow = 0
        minCol = 0
        maxRow = len(matrix)-1
        maxCol = len(matrix[0])-1
        
        # loop through perimeter and record values
        while minRow <= maxRow and minCol <= maxCol:
            # record alone the top edge
            for c in range(minCol,maxCol+1):
                sol.append(matrix[minRow][c])
        
            # record along the right edge
            for r in range(minRow+1,maxRow+1):
                sol.append(matrix[r][maxCol])
            
            # record along the bottom edge
            # we don't want to record it if there's only one row in this perimeter
            if minRow < maxRow:
                for c in reversed(range(minCol,maxCol)):
                    sol.append(matrix[maxRow][c])
                
            # record along the left edge
            # we don't want to record it if there's only one column in this perimeter
            if minCol < maxCol:
                for r in reversed(range(minRow+1,maxRow)):
                    sol.append(matrix[r][minCol])
            
            # update perimeter
            minRow += 1
            maxCol -= 1
            maxRow -= 1
            minCol += 1
            
        return sol