# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if root is None:
            return root

        LCA = []
        self._getLCA(LCA, root, p, q)
        
        # if the LCA isn't found return None
        if not LCA:
            return None
        return LCA[0]
    
    def _getLCA(self, LCA, node, p, q):
        # base case
        if node is None:
            return [False, False] # return format: [pFound, qFound]
        left = self._getLCA(LCA, node.left, p, q)
        right = self._getLCA(LCA, node.right, p, q)
        
        # undo the recursive stack if we've found the LCA
        if LCA:
            return [True, True]
        
        pFound = left[0] or right[0] or node == p
        qFound = left[1] or right[1] or node == q
        
        # we found our LCA!
        if pFound and qFound:
            LCA.append(node)
            
        return [pFound, qFound]
    
    