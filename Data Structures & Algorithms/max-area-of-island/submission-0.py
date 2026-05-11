class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        new_area = 0
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            current_area = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols
                        or (nr, nc) in visited or grid[nr][nc] == 0):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    current_area += 1
            return current_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    new_area = bfs(r, c)
                    max_area = max(max_area, new_area)
                    new_area = 0

        return max_area
