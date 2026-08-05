# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bfs(node, value):
            if node is None:
                return TreeNode(value)
            if value > node.val:
                node.right = bfs(node.right, val)
            else:
                node.left = bfs(node.left, val)
            
            return node # we need to do this to reconstruct the tree correctly, as each of then need to return the correct node to it's parent to reconstruct it from the bottom

        return bfs(root, val)