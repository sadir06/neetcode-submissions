class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))  # FIX 1: Mark start node as visited immediately!
            
            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    if (nr < 0 or nc < 0 or nr >= rows or 
                        nc >= cols or (nr, nc) in visited or 
                        grid[nr][nc] == "0"): # FIX 2: Stop if it's water!
                        continue
                    
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands