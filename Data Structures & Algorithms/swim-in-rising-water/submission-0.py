class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0)) # We never swin back

        
        while min_heap:
            max_elevation_so_far, x, y = heapq.heappop(min_heap)
            if x == ROWS - 1 and y == COLS - 1: # We have reached the correct square!
                return max_elevation_so_far

            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    new_max = 0
                    new_max = max(max_elevation_so_far, grid[nr][nc])
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (new_max, nr, nc))