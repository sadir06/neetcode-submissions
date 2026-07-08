# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        queue = deque([(root, float("-inf"))])
        while queue: # We will explore all values
            store, maxnum = queue.popleft() # now I understand why we have to popleft. I used to learn off questions by heart and not understand why we had to do this, but now I get it, it's so that we can access the current value, play around with it, and keep the chain moving
            if store.val >= maxnum:
                maxnum = store.val
                goodNodes += 1
            if store.left:
                queue.append((store.left, maxnum))
            if store.right:
                queue.append((store.right, maxnum))

        return goodNodes