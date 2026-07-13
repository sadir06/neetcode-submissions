class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cr, cc = queue.popleft()
                for dr, dc, in directions:
                    nr, nc = dr + cr, dc + cc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == "1"):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1": # If we find a 1, that means we can start searching for an island
                    bfs(r, c) # This will find 1 full island, and fill out visited, so that we never touch those squares again
                    islands += 1

        return islands