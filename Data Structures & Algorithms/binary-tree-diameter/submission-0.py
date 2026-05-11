# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 # leftHeight + rightHeight

        def dfs(root):
            nonlocal res 

            if not root:
                return 0

            left = dfs(root.left) # Use this type of recursion to reach the bottom of the tree
            right = dfs(root.right)
            res = max(res, left + right) # Use this to do the maximum diameter calculation

            return 1 + max(left, right) # Add one at each level

        dfs(root)

        return res