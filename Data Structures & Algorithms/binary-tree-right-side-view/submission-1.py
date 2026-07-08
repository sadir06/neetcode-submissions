# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        output = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                store = queue.pop()
                if store.left: # store this first
                    queue.appendleft(store.left)
                if store.right:
                    queue.appendleft(store.right)
                if i == level_size - 1:
                    output.append(store.val) 
        return output