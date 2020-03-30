class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # base case for when root is none
        if root is None:
            return None
        if root.val == key:
            # if want to delte the current node, we must find its successor if it has a child
            # if it has two children, it doesn't matter which successor you pick
            if root.left:
                # the successor on the left will be the left child's rightmost leaf
                successor = root.left
                while successor.right:
                    successor = successor.right
                root.val = successor.val
                root.left = self.deleteNode(root.left, successor.val)
            elif root.right:
                # the successor on the right will the be right child's leftmost leaf
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
            # if it has no kids, return None to delete itself
            else:
                return None
        # if the node doesn't match the value to be deleted, then we can reduce the problem to 
        # deleting a value from one of its subtrees
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root