"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # OK so we need to go through the adjacency list and create new nodes and edeges that don't reference the old ones
        clones = {} # Everytime we clone a new "room", we write it down here old_node : newly_cloned_node
        def dfs(node):
            if not node:
                return None # handles empty graphs
            if node in clones:
                return clones[node] # If we have already created this node, just return the newly created node

            copy = Node(node.val) # Take the value of the current node, and create a new node object with no neighbours currently
            clones[node] = copy # old_val : new_val
            for neighbor in node.neighbors:
                output = dfs(neighbor) # Create a new neighbor for each one
                copy.neighbors.append(output)

            return copy
        return dfs(node)
        