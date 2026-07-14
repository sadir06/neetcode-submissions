class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        inf = 2147483647 # this will be the infinite value
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 0: # We always start the search in a 0
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            cr, cc = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue # We don't use this, it is ahh
                
                if grid[nr][nc] == -1:
                    continue # It is ahh again
                
                if grid[nr][nc] == inf:
                    grid[nr][nc] = grid[cr][cc] + 1
                
                queue.append((nr, nc))
                visited.add((nr, nc))

        return # We modify in place