"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        We have 2 nodes P, Q, return the LCA, however, here, each of those nodes has a reference to its parent node. The definition for a node si the val, the left the right and the parent. 
        """
        ordering = []
        searching = set()

        def dfs(node, state): # Given a node keep going up to the top, and adding it to the input   
            if state == "p":
                ordering.append(node)
            else:
                searching.add(node)
            if node.parent is None:
                return None # We end here
            return dfs(node.parent, state)
        dfs(p, "p")
        dfs(q, "q")
        for node in ordering:
            if node in searching:
                return node


