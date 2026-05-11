from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        
        # Matrix to keep track of reachable cells from each ocean
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(sources, ocean_reachable):
            q = deque(sources)
            # Mark initial sources as reachable
            for r, c in sources:
                ocean_reachable[r][c] = True
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds and if we haven't visited this cell for this ocean
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        not ocean_reachable[nr][nc] and 
                        heights[nr][nc] >= heights[r][c]): # Flowing "uphill"
                        
                        ocean_reachable[nr][nc] = True
                        q.append((nr, nc))

        # Define starting points for both oceans
        pacific_starts = []
        atlantic_starts = []

        for r in range(ROWS):
            pacific_starts.append((r, 0))          # Left edge
            atlantic_starts.append((r, COLS - 1))  # Right edge
        for c in range(COLS):
            pacific_starts.append((0, c))          # Top edge
            atlantic_starts.append((ROWS - 1, c))  # Bottom edge

        # --- THE MISSING STEP: Run the BFS ---
        bfs(pacific_starts, pac)
        bfs(atlantic_starts, atl)

        # Find cells reachable by both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res