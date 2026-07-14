class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                

        while queue and fresh_count > 0:
            for i in range(len(queue)): # This one will run once for all of the rotten fruits that we have accumulated in queue, and for all the newly rotten fruits in the next run, and so on. 
                cr, cc = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) and grid[nr][nc] == 1: # This means the new one is a valid row that is not out of bounds, and is also a fresh fruit, this means that it will become rotten
                        queue.append((nr, nc))
                        grid[nr][nc] = 2 # Turn that fruit rotten
                        fresh_count -= 1
            time += 1

        return time if fresh_count == 0 else -1
