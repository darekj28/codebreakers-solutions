class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # helper function to check if subtree values are within the restraints of a bst
        return self._areNodesWithinBounds(root, -math.inf, math.inf)
    
    def _areNodesWithinBounds(self, node, lowerBound, upperBound):
        # base case
        if node is None:
            return True
        # check if node is invalid
        if node.val < lowerBound or node.val > upperBound:
            return False
        # check if its children are valid
        # the current node's value is an upper bound for all nodes to its left
        left = self._areNodesWithinBounds(node.left, lowerBound, node.val-1)
        # the current node's value is a lower bound for all nodes to its right
        right = self._areNodesWithinBounds(node.right, node.val+1, upperBound)
        return left and right