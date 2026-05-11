class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        row, col = len(grid), len(grid[0])
 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                r2, c2 = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r2, dc + c2

                    if (nr < 0 or nc < 0 or nr >= row or
                        nc >= col or grid[nr][nc] == "0"):
                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
