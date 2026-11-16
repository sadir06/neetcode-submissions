# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """
        Given the root node of a binary search tree, and 2 integers low and high, return the sum of values of all nodes with a value in the inclusive range. Simple, just do DFS, with an O(1) check to see if it is in between, and add it to a carried nonlocal sum. This is O(V + E).
        total_sum = 0
        def dfs(node):
            if not node:
                return
            nonlocal total_sum
            dfs(node.left)
            dfs(node.right)
            if low <= node.val <= high:
                total_sum += node.val
        dfs(root)
        return total_sum
        Now the smarter solution, since this is a binary search tree, we can do a smarter search in the tree. Do a recursive loop for each node: if the value is in between search both children, if it is lower than low check only the right branch, else the left one. 
        """
        total_sum = 0
        def dfs(node):
            if not node:
                return
            nonlocal total_sum
            if low <= node.val <= high:
                total_sum += node.val
                dfs(node.left)
                dfs(node.right)
            elif low > node.val:
                dfs(node.right)
            elif high < node.val:
                dfs(node.left)
        dfs(root)
    
        return total_sum