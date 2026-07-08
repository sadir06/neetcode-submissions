# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        output = []
        while queue:
            level_size = len(queue) # We take a snapshot of how many values are on the current list
            temp = []
            for _ in range(level_size):
                store = queue.pop()
                temp.append(store.val)
                if store.left:
                    queue.appendleft(store.left)
                if store.right:
                    queue.appendleft(store.right)
            output.append(temp)
        return output

