class Solution(object):
    def spiralOrder(self, matrix):
        # initialize solution
        sol = []
        # check for an empty input
        if len(matrix) == 0:
            return sol
        # initialize bounds for perimeter to traverse
        minR = 0
        minC = 0
        maxR = len(matrix)-1
        maxC = len(matrix[0])-1
        
        # loop through perimeter and record values
        while minR <= maxR and minC <= maxC:
            # record alone the top edge
            for c in range(minC,maxC+1):
                sol.append(matrix[minR][c])
        
            # record along the right edge
            for r in range(minR+1,maxR+1):
                sol.append(matrix[r][maxC])
            
            # record along the bottom edge
            # we don't want to record it if there's only one row in this perimeter
            if minR < maxR:
                for c in reversed(range(minC,maxC)):
                    sol.append(matrix[maxR][c])
                
            # record along the left edge
            # we don't want to record it if there's only one column in this perimeter
            if minC < maxC:
                for r in reversed(range(minR+1,maxR)):
                    sol.append(matrix[r][minC])
            
            # update perimeter
            minR += 1
            maxC -= 1
            maxR -= 1
            minC += 1
            
        return sol