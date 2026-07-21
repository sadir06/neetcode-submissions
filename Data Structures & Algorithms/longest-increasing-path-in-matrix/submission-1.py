class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        max_len = 0
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        dp = {}
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            current_length = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    output = 1 + dfs(nr, nc)
                    current_length = max(output, current_length)
            dp[(r, c)] = current_length

            return dp[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                current_len = dfs(r, c)
                max_len = max(max_len, current_len)

        return max_len