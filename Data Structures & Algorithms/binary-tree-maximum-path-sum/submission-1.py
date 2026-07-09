# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf") # Make this global
        def recurse(root):
            # This takes in the maximum single path gain that this node can contribute to its parent. 
            if not root:
                return 0 # If we hit an empty node like None, we return 0, because we are calculating sums, remember
            left = max(recurse(root.left), 0) # We don't want negative sums
            right = max(recurse(root.right), 0)
            self.max_sum = max((root.val + left + right), self.max_sum) # Compare the V shape with the global high score
            return root.val + max(left, right) # Return the node's curernt value + the value of the highest of the 2 children of the current node upwards for the highest calculation -> This makes things faster as we eliminate smaller sums
        recurse(root)
        return self.max_sum