# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val):
                # We immediately return here because we have found the point of divergence
                return root
            elif root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val == p.val:
                # This means that root is equal to the val
                return p
            else:
                return q
        