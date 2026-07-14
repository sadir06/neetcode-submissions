class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable, atlantic_reachable = set(), set()
        result = []
        def dfs(r, c, visited_set, previous_height):
            if (r < 0 or r >= ROWS or 
                    c < 0 or c >= COLS or 
                    (r, c) in visited_set or 
                    heights[r][c] < previous_height):
                    return
            visited_set.add((r, c))

            for dr, dc in directions:
                dfs(dr + r, dc + c, visited_set, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c])
            dfs(0, c, pacific_reachable, heights[0][c])


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append(([r, c]))

        return result
         
                    