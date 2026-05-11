# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            stack.append((node_p.right, node_q.right))
            stack.append((node_p.left, node_q.left))

        return True