class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        matrix.reverse() # Simple and easy vertical flip

        for r in range(ROWS - 1):
            for c in range(r, COLS): # We only want to swap once, if we did it twice, that would just reset the matrix
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        return