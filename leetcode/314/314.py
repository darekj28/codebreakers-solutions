# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # deal with base case
        if root is None:
            return []
        
        # map node columns to list of nodes
        colToNodes = collections.defaultdict(list)
        
        # instantiate queue and base case variables for bfs
        queue = collections.deque()
        column = 0
        queue.append([root, column])
        
        # bfs
        leftMostColumn = 0 
        while queue:
            currNode, column = queue.pop()
            leftMostColumn = min(leftMostColumn, column)
            colToNodes[column].append(currNode.val)
            # add children to queue
            if currNode.left:
                queue.appendleft([currNode.left, column-1])
            if currNode.right:
                queue.appendleft([currNode.right, column+1])
                
        # instantiate solution variable
        verticalNodesLists = []
        currColumn = leftMostColumn
        while currColumn in colToNodes:
            verticalNodesLists.append(colToNodes[currColumn])
            currColumn += 1
        return verticalNodesLists
        