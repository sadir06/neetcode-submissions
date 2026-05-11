class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        # visited set not necessary here, just change the grid

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_oranges = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1

                if grid[r][c] == 2:
                    queue.append((r, c))

        if fresh_oranges == 0:
            return 0

        while queue and fresh_oranges > 0:
            
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc


                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue

                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2 
                    fresh_oranges -= 1
                    queue.append((nr, nc))
            minutes += 1

                

        return minutes if fresh_oranges == 0 else -1

