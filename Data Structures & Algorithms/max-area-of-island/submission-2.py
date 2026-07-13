class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0]), # the number of rows are hte number of sublists in the list, the cols are the length of the sublists inside the list (m * n)
        visited = set()
        self.max_volume = 0

        def bfs(r, c):
            # import collections -> you need this for the deque
            queue = deque()

            queue.append((r, c))
            visited.add((r, c))
            current_volume = 1 # We found the current block
            while queue:
                cr, cc = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc)) 
                        current_volume += 1
                self.max_volume = max(self.max_volume, current_volume)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    bfs(r, c)    
                
        return self.max_volume