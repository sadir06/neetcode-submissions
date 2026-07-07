# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        
        def getHeight(root):
            if not root:
                return 0
            dr, dl = getHeight(root.right), getHeight(root.left)
            d = dl + dr
            self.maxPath = max(self.maxPath, d)
            return 1 + max(dr, dl)
        getHeight(root)
        return self.maxPath