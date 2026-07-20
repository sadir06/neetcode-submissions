class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        if not grid:
            return None

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            cr, cc = queue.popleft()
            current_distance = 0

            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                current_distance += 1
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[cr][cc] + 1
                    queue.append((nr, nc))
