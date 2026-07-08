# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                store, floor, ceiling = queue.popleft() # this gives us one node
                if not (floor < store.val < ceiling):
                    return False
                if store.left:
                    queue.append((store.left, floor, store.val))
                if store.right:
                    queue.append((store.right, store.val, ceiling))
            
        return True