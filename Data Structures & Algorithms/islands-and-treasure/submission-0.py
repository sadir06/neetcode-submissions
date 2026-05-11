class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        distance = 0
        while queue:

            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if grid[nr][nc] == -1 or (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    grid[nr][nc] = distance + 1
                    queue.append((nr, nc))

            distance += 1

