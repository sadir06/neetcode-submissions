# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        elif p.val != q.val:
            return False
        
        # If we have reached this point, we can just recursively check the left and right, because we have written out the conditoins above!
        left_is_same = self.isSameTree(p.right, q.right)
        right_is_same = self.isSameTree(p.left, q.left)
        return left_is_same and right_is_same