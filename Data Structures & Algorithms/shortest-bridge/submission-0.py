from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        We have an nxn binary (0, 1) matrix grid where 1 represents land and 0 represents water. An island is a 4-directionally connected group of 1s not connected to any other ones. There are exactly 2 islands in grid, no more no less. We may change 0s to 1s to connect the 2 islands to form one island. Return the min number of 0s you must flip to connect the 2 islands. This is a very interseting question, you need to start by finding and them mapping out the actual islands. Once you do, you need to find the closest 2 points using something like the manhattan distance formula, so if you just check all of the points against each other, and find the shortest distance, then you can do search starting from multiple sources (so BFS) till both points meet, and you take the shortest path among those points. 
        """

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        store = set()
        found = False
        def bfs(r, c):
            queue = deque()
            store.add((r, c))
            queue.append((r, c))
            while queue:
                cr, cc = queue.popleft()

                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in store:
                        store.add((nr, nc))
                        queue.append((nr, nc))
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bfs(r, c)
                    found = True
                    break
            if found:
                break
        count = 0
        queue_2 = deque()
        
        for r, c in store:
            queue_2.append((r, c))
        
        while queue_2:
            n = len(queue_2)
            for _ in range(n):
                cr, cc = queue_2.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in store and grid[nr][nc] == 0:
                        queue_2.append((nr, nc))
                        store.add((nr, nc)) # Don't go into explored territory
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in store and grid[nr][nc] == 1:
                        return count

            count += 1
        return
            

        