class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        output = []
        top, bottom, left, right = 0, ROWS - 1, 0, COLS - 1 

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                output.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                output.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for r in range(right, left - 1, -1):
                    output.append(matrix[bottom][r])
                bottom -=1
            if left <= right:
                for c in range(bottom, top - 1, -1):
                    output.append(matrix[c][left])
                left += 1
            

        return output