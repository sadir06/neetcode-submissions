class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9): # Here we check the rows for duplicates using a python set (hash set), and return False if there are any duplicates
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i]) 


        for col in range(9): # This does the same check as above, but for the cols instead
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        # Now we have to do a grid check for the 3x3s

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i # These 2 functions always apply: "//" for rows 
                    col = (square % 3) * 3 + j # And % for cols. This will always work
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True # If all checks are successfully passed, return True
        