class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_path = []
        self.visited = set()

        rows, cols = len(board), len(board[0]) # We have to do this, as the column length is the length of one of the sublists, and the row length is the number of sublists
        def backtrack(r, c, i): # row and column and index of hte word that you are currently on
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in self.visited or board[r][c] != word[i]:
                return False
            
            self.visited.add((r, c))
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                output = backtrack(nr, nc, i + 1)
                if output: # If any of those 4 paths have found the actual value, we return True and have found the word 
                    return True
            self.visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                # This picks one letter in the whole grid
                if backtrack(r, c, 0) == True:
                    return True
        return False #  If nothing has been found we return False