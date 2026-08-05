# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return 
        
        if root.val == key:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right # these scenarios are easy to deal with 

            cur = root.right

            while cur.left:
                cur = cur.left
            root.val = cur.val

            root.right = self.deleteNode(root.right, root.val)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        
        return root # Return the root as asked once all recursion is completed (and also to return the root to properply assign root.left/root.right)