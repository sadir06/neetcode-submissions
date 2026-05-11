from copy import deepcopy

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # LeetCode represents an empty graph as None
        if not node:
            return None
        
        # Use the function directly to avoid naming conflicts with 'copy'
        return deepcopy(node)