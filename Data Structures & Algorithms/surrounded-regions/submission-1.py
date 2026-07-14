class Solution:
    def solve(self, board: List[List[str]]) -> None:
            visited = set() # We will use this set to store Os that are connected to edges which are impossible to be fully surrounded by Xs as that would mean they can't be connected to one on the edge. Then we will iterate over all of the inner rows and cols (excluding all of the edges), and if there are any Os that are not in our visited set, we will immediately turn them into Xs. 
            queue = deque()
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            ROWS, COLS = len(board), len(board[0])

            for r in range(ROWS):
                if board[r][0] == "O":
                    queue.append((r, 0))
                    visited.add((r, 0))
                if board[r][COLS - 1] == "O":
                    queue.append((r, COLS - 1))
                    visited.add((r, COLS - 1))
            for c in range(COLS):
                if board[0][c] == "O":
                    queue.append((0, c))
                    visited.add((0, c))

                if board[ROWS - 1][c] == "O":
                    queue.append((ROWS - 1, c))
                    visited.add((ROWS - 1, c))

            while queue:
                cr, cc = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and board[nr][nc] == "O":
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            for r in range(1, ROWS - 1):
                for c in range(1, COLS - 1):
                    if board[r][c] == "O" and (r, c) not in visited:
                        board[r][c] = "X"

            return # We don't need to return anything, it's just good to have

                            