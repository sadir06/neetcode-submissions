class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.visited = set()

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            self.visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in self.visited and board[nr][nc] == word[i]:
                    if dfs(nr, nc, i + 1):
                        return True
            self.visited.remove((r, c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1):
                        return True
        return False