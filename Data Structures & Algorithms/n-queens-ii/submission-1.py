class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        res = 0

        def backtrack(r):
            nonlocal res # Links to the outer variable insted of defining a new local one inside
            if r == n: # Reached the final row
                res += 1 # this is the base case, once we reach the final row, we increment result and return, because the last row will always have a square to place the queen on.
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag: # these are ALL occupied by other queens
                    continue # We can't touch these, skip

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
    
        return res # Result is incrememented at the end of every path once we have found room to place a queen