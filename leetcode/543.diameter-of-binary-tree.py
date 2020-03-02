# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Motivation:
Note that the length of the binary tree is defined as the number of edges between two nodes.
Given this definition, for any node to know what the length of the longest path it is a part
of, it must retreive information from its children. Since this is necessary, the problem naturally
lends itself towards a post order traversal (dfs). Since the root is not necessarily part of the
longest path, it is necessary to send more information than just the current node's height from
child to parent. In the solution below, each child returns both its height and the longest path
seen so far.

Time Complexity:
The post order traversal visits each node once, leading to a time complexity of O(n), linear in the
number of nodes. 

Space Complexity:
The space complexity is the height of the binary tree, taken up by the recursive call stack. Since
the height of the tree can be the whole tree itself (one long vine), the space complexity is O(n)
as well.
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.getLongestPath(root)[1]
    
    def getLongestPath(self, currNode):
        # Base Case
        if currNode is None:
            return [0,0] # [height from the bottom of the tree, longest path so far]

        # retreiving data from children
        leftData = self.getLongestPath(currNode.left)
        rightData = self.getLongestPath(currNode.right)

        # calculating current node's data given data from children
        currNodeHeight = max(leftData[0], rightData[0]) 
        longestPathSoFar = max(leftData[1], rightData[1], leftData[0]+rightData[0])
        return [currNodeHeight + 1, longestPathSoFar]