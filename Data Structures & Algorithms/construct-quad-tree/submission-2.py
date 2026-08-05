"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, n):
            first_val = grid[r][c]
            is_same = True
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != first_val:
                        is_same = False
                        break
                if not is_same:
                    break
            if is_same:
                return Node(val=bool(first_val), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            half = n // 2
            top_left = dfs(r, c, half)
            top_right = dfs(r, c + half, half)
            bottom_left = dfs(r + half, c, half)
            bottom_right = dfs(r + half, c + half, half)

            return Node(val = True, isLeaf = False, topLeft=top_left, topRight=top_right, bottomLeft=bottom_left, bottomRight=bottom_right)

        return dfs(0, 0, len(grid))