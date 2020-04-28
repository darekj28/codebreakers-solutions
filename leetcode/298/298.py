# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self._getLongestConsecutive(root, None, 0)
    
    # recursive helper function
    def _getLongestConsecutive(self, root, parentValue, consecutiveSoFar):
        # base case
        if root is None:
            return 0
        
        # update length of consecutive nodes ending at this node
        if parentValue is None or root.val == parentValue + 1:
            consecutiveSoFar += 1
        else:
            consecutiveSoFar = 1
        
        # get longest consecutive nodes from children
        leftLongest = self._getLongestConsecutive(root.left, root.val, consecutiveSoFar)
        rightLongest = self._getLongestConsecutive(root.right, root.val, consecutiveSoFar)
        
        # return the longest consecutive node of children and current node
        return max(consecutiveSoFar, leftLongest, rightLongest)