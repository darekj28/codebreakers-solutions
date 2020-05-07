# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if root is None:
            return root
        
        # keep track of current's node's children
        leftChild = root.left
        rightChild = root.right
        
        # post order traversal since we want the youngest child nodes to link
        leftResult = self.flatten(leftChild)
        rightResult = self.flatten(rightChild)
        
        # turn the nodes into a list. Note the list follows the order:
        # root -> left child ... last node in left subtree -> right child
        root.left = None
        if leftChild:
            root.right = leftChild
            leftResult.right = rightChild
        
        # return the node at the end of the list
        if rightResult:
            return rightResult
        if leftResult:
            return leftResult
        return root