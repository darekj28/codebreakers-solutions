class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if root is None:
            return None
        # invert all nodes in left subtree
        left = self.invertTree(root.left)
        # invert all nodes in right subtree
        right = self.invertTree(root.right)
        # invert the children of the current node
        root.left = right
        root.right = left
        return root