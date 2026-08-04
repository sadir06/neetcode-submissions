# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return 
            res.append(node.val) # Add the value first
            dfs(node.left) # Go as far left as possible ading values
            dfs(node.right) # try the right values too, add those nodes as well
        dfs(root)
        return res