"""
Motivation:
Immediately upon inspection of the problem, we should observe that our solution should take 
advantage of the sorted properties of the matrix to achieve a solution that would be reasonable
for interviews. (The naive solution of searching through the matrix linearly defeats the purpose
of the problem.) Here the trick is to start your search at either the bottom left corner or top 
right corner fo the matrix. By starting at the "extreme points" of the matrix, we can cut the space
we are searching through for the target very easily. Take the bottom left corner for example: if 
the target is greater than the value, then the target (if in the matrix) must involve a column to 
the right, since all values in the current row are also too small. Similarly, if the target is 
smaller than the value in the bottom left corner, then the solution cannot involve the current 
column or any column to its left. 

Time Complexity:
The time complexity is linear to the number of rows and columns in the matrix should the target not
exist in the matrix.

Space Complexity:
The space complexity is constamt since we only use a few variables for the algorithm. 
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        numRows = len(matrix)
        # Base Case to ensure the matrix isn't empty
        if numRows == 0:
            return False
        numCols = len(matrix[0]) 
        
        # initialize starting position for search to bottom left corner
        currRow = numRows-1
        currCol = 0
        while currCol < numCols and currRow >= 0:
            currValue = matrix[currRow][currCol]
            if currValue == target:
                return True
            # if the candidate is greater than the target, and in the matrix, the target must be in
            # a higher row
            elif currValue > target:
                currRow -= 1
            # if the candidate is smaller than the target, and in the matrix, the target must be to
            # the right
            else:
                currCol += 1
        # if we get out of the array bounds it means the target isn't in the matrix.
        return False