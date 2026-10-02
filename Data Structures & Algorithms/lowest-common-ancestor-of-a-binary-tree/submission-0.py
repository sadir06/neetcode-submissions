# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        The lowest common ancestor is defined between 2 nodes p and q as the lowest node t that has both p and q as descendents. Basically we need to find the 2 nodes p and q, and there are a couple of posibilities. either they are on opposite sides of the tree, and that means that the root is the point, but essentially it is the earliest point that they are separated, where they are on different sides. So we keep going as lnog as they are both on the left and right, and the first point where they break off, we return that node. There is another option, when they aren't on the same level, and at that point, it's the highest one that is the answer. Implementing this is easier said than done though, how do we determine which side of the tree they are on?? Do we just do a recursive search until we find them, and check if they are on the left or right at each node??? And once they are on different sides, or once one of our nodes equals them, we return the answer? And we go level by level, we can do that with like BFS right?
        """

        def dfs(node):
            if not node:
                return None

            if node is p:
                return p
            if node is q:
                return q # If we ever hit these points, they are the LCA, because it means that they are on 2 different levels, and the LCA will just be those values. 
            left, right = dfs(node.left), dfs(node.right)
            if left and right:
                return node # This is the LCA
            if left and right is None: # Right found nothing
                return left
            elif right and left is None:
                return right     

            if right is None and left is None:
                return None

        return dfs(root)
            




