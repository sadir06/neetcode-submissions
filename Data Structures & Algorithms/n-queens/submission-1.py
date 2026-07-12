class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.current_path = []
        self.cols, self.pos_diag, self.neg_diag = set(), set(), set()
        def backtrack(r):
            if r == n: # If we have reached the last row, we exit
                self.results.append(self.current_path[:])
                return
            for c in range(n):
                if c in self.cols or (r + c) in self.pos_diag or (r - c) in self.neg_diag: # Is safe from attacks
                    continue # We cannot place anything here
                else:
                    row_string = ("." * c) + "Q" + ("." * (n - c - 1))
                    self.current_path.append(row_string)
                    self.cols.add(c)
                    self.pos_diag.add((r + c))
                    self.neg_diag.add((r - c))
                    backtrack(r + 1)
                    self.current_path.pop()
                    self.cols.remove(c)
                    self.pos_diag.remove((r + c))
                    self.neg_diag.remove((r - c))
        backtrack(0) # Start from row 0
        return self.results