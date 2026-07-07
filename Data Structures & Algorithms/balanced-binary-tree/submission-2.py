# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # We can start off by exploring the left and right of all using DFS with recursion
        # We can create a left height and a right height, and this will allow us to keep track of the lowest left and lowest right, and give us the specific heights, nad we check if they differ by one

        def get_height(root):
            if not root:
                return 0
            left_height = get_height(root.left)
            right_height = get_height(root.right)
            if left_height == -1 or right_height == -1:
                return -1 
            if abs(right_height - left_height) > 1:
                return -1
            return max(right_height, left_height) + 1
        return get_height(root) != -1