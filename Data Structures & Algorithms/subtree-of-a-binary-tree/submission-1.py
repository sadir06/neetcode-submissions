# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_recur(self, p, q):
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        elif p.val != q.val:
            return False
        
        # If we have reached this point, we can just recursively check the left and right, because we have written out the conditoins above!
        left_is_same = self.get_recur(p.right, q.right)
        right_is_same = self.get_recur(p.left, q.left)
        return left_is_same and right_is_same 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True # They have to be the same
        elif not root:
            return False
        elif not subRoot:
            return False

        if self.get_recur(root, subRoot): return True

        else:  
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        # We need to add some recursion logic here

        return False # We need a way to return false if the recursion is over and we haven't reached anything

