# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.count = 0
        self.ans = 0
        def in_order(node):
            if not node:
                return

            in_order(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.val
                return
            in_order(node.right)
        in_order(root)

        return self.ans